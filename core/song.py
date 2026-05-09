import asyncio
import threading
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from PyQt6.QtCore import QObject, pyqtSignal
from core.song_cover import thumbnail_saver as thumbnail_s

class SpotifyListener(QObject):
    # 3 strings for artist name, song name and  thumbnail (bytes)
    song_updated = pyqtSignal(str, str, bytes)

    def __init__(self):
        super().__init__()
        self.manager = None
        self.session = None

    def start_listener(self):
        thread = threading.Thread(target=self._run_async_loop, daemon=True)
        thread.start()

    def _run_async_loop(self):
        asyncio.run(self._setup_events())

    # attach windows smtc event callbacks
    async def _setup_events(self):
        self.manager = await MediaManager.request_async()
        await self._spotify_info()
        # when session changes, say spotify is closed and then reopened
        # --> reattach the spotify session without the need for restarting
        #     the entire app
        self.manager.add_sessions_changed(self._on_sessions_changed)

    async def _spotify_info(self):
        if self.manager is None:
            return

        sessions = self.manager.get_sessions()
        for session in sessions:
            app_id = session.source_app_user_model_id.lower()
            if "spotify" in app_id:
                self.session = session
                self.session.add_media_properties_changed(self._on_properties_changed)
                # forcing immediate fetch on startup
                await self._fetch_song_info(self.session)
                return
        self.session = None

    def _on_sessions_changed(self, manager, args):
        asyncio.run(self._spotify_info())

    def _on_properties_changed(self, session, args):
        # executing fetch function when the windows event triggers
        asyncio.run(self._fetch_song_info(session))

    async def _fetch_song_info(self, session):
        try:
            info = await session.try_get_media_properties_async()

            if info:
                # placeholder
                title = info.title if info.title else "Unknown title"
                artist = info.artist if info.artist else "Unknown artist"
                #thumbnail_path = "assets/default_cover.png"
                image_bytes = b""       # <-- empty byte string to get no NoneType error

                if info.thumbnail:
                    image_bytes = await thumbnail_s(info.thumbnail)

                self.song_updated.emit(title, artist, image_bytes)

        except Exception as e:
            print(f"bg fetch error: {e}")

if __name__ == "__main__":
    pass
    #asyncio.run(song_info())
