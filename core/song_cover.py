import asyncio
from winrt.windows.storage.streams import \
    DataReader, IRandomAccessStreamReference, Buffer, InputStreamOptions
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from PIL import Image

async def thumbnail_saver(thumbnail: IRandomAccessStreamReference):
    # opening the stream buffer to get image data 
    stream = await thumbnail.open_read_async()
    buffer = Buffer(stream.size)
    await stream.read_async(buffer, buffer.capacity, InputStreamOptions.NONE)

    reader = DataReader.from_buffer(buffer)
    thumb_bytes = bytearray(buffer.length)
    byte_buffer = reader.read_bytes(thumb_bytes)

    thumb_path = "core/song_image.png"
    with open(thumb_path, "wb") as file:
        file.write(thumb_bytes)

    # image cropping:
    thumb_path_final = "core/song_cover.png"
    with Image.open(thumb_path) as img:
        # (l, u, r, b)
        box = (33, 0, 267, 234)
        final_img = img.crop(box)
        final_img.save(thumb_path_final)

'''     # Calling the function in song.py
async def song_cover_fetch():
    manager = await MediaManager.request_async()
    session = manager.get_current_session()
    app_id = session.source_app_user_model_id.lower()

    if "spotify" in app_id:
        info = await session.try_get_media_properties_async()
        await thumbnail_saver(info.thumbnail)
'''
# asyncio.run(song_cover_fetch())
