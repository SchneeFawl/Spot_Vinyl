import asyncio
import threading
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from PyQt6.QtCore import QObject, pyqtSignal
from song_cover import thumbnail_saver as thumbnail_s

class SpotifyListener(QObject):
    # 3 strings for artist name, song name and  thumbnail
    song_updated = pyqtSignal(str, str, str)

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
        self._spotify_info()
        # when session changes, say spotify is closed and then reopened
        # --> reattach the spotify session without the need for restarting
        #     the entire app
        self.manager.add_sessions_changed(self._on_sessions_changed)

    def _spotify_info(self):
        if self.manager is None:
            return

        sessions = self.manager.get_sessions()
        for session in sessions:
            app_id = session.source_app_user_model_id.lower()
            if "spotify" in app_id:
                self.session = session
                self.session.add_media_properties_changed(self._on_properties_changed)
                # forcing immediate fetch on startup
                self._on_properties_changed(self.session, None)
                return
        self.session = None

    def _on_sessions_changed(self, manager, args):
        self._spotify_info()

    def _on_properties_changed(self, session, args):
        # executing fetch function when the windows event triggers
        asyncio.run(self._fetch_song_info(session))

    async def _fetch_song_info(self, session):
        info = await session.try_get_media_properties_async()
        if info:
            title = info.title
            artist = info.artist
            thumbnail_path = await thumbnail_s(info.thumbnail)
            #print(title, artist)

            if thumbnail_path:
                self.song_updated.emit(title, artist, thumbnail_path)

if __name__ == "__main__":
    pass
    #asyncio.run(song_info())
