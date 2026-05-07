import asyncio
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
# from winrt.windows.storage.streams import \
#    DataReader, Buffer, InputStreamOptions, IRandomAccessStream, IRandomAccessStreamReference
from song_cover import thumbnail_saver as thumbnail_s

async def song_info():
    # song details
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    app_id = current_session.source_app_user_model_id.lower()
    TARGET_ID = "spotify"
    #print(app_id)

    if current_session and TARGET_ID in app_id:
        info = await current_session.try_get_media_properties_async()

        if info:
            title = info.title
            artist = info.artist
            thumbnail_info = info.thumbnail
            thumbnail = await thumbnail_s(thumbnail_info)
            #print(title, artist)
            return title, artist, thumbnail

if __name__ == "__main__":
    asyncio.run(song_info())
