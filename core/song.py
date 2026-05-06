import asyncio
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from winrt.windows.storage.streams import \
    DataReader, Buffer, InputStreamOptions
# from winrt.windows.foundation import IAsyncOperation

async def spotify_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    app_id = current_session.source_app_user_model_id.lower()
    TARGET_ID = "spotify"
    # print(app_id)

    if current_session and TARGET_ID in app_id:
        info = await current_session.try_get_media_properties_async()

        if info:
            title = info.title
            artist = info.artist
            # print(title, artist)
            return title, artist

asyncio.run(spotify_info())