import sys
import ctypes
from pathlib import Path

# PATH FIX FOR PYINSTALLER!!!
if getattr(sys, "frozen", False):
    # running as packaged exe in the _MEIPASS temp folder
    ROOT_DIR = Path(sys._MEIPASS)
    sys.path.append(str(ROOT_DIR))
else:
    # running normally from terminal
    ROOT_DIR = Path(__file__).resolve().parent.parent
    sys.path.append(str(ROOT_DIR))
    sys.path.append(str(ROOT_DIR / "ui"))

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import \
    QPixmap, QMovie, QFontMetrics, QFontDatabase, QFont, QAction, QIcon
from PyQt6.QtWidgets import \
    QApplication, QMainWindow, QLabel, QSystemTrayIcon, QMenu, QStackedWidget, QWidget
from buttons import *
from core.song import SpotifyListener
from settings_menu import *
from core.config_manager import ConfigManager
from core.discord import send_discord_webhook

ASSETS_DIR = ROOT_DIR / "assets"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # load icon bytes for discord webhook
        icon_path = ASSETS_DIR / "icon.png"
        with open(icon_path, "rb") as f:
            self.icon_bytes = f.read()

        self.setWindowTitle("Spot_Vinyl")
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setFixedSize(500, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)    # for transparent bg

        # config
        # if running as exe then config file stays in the same dir as exe file
        if getattr(sys, "frozen", False):
            config_file = Path(sys.executable).parent / "config.json"
        else:    # if running from terminal, then in ./core dir
            config_file = ROOT_DIR / "core" / "config.json"
        self.config = ConfigManager(config_file)

        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon(str(ASSETS_DIR / "icon.png")))

        tray_menu = QMenu()
        show_hide_action = QAction("Show / Hide", self)
        quit_action = QAction("Quit", self)
        tray_menu.addAction(show_hide_action)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)

        show_hide_action.triggered.connect(self.toggle_window)
        quit_action.triggered.connect(QApplication.quit)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # custom font (04B_03.TTF)
        font_id = QFontDatabase.addApplicationFont(str(ASSETS_DIR / "04B_03.TTF"))
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 16)        # font size = 15

        BG_LABEL = QLabel(self)
        BG_LABEL.setGeometry(0, 0, 500, 500)
        bg_path = ASSETS_DIR / "bg_main.png"
        BACKGROUND = QPixmap(str(bg_path))
        BG_LABEL.setPixmap(BACKGROUND)
        BG_LABEL.setScaledContents(True)

        # create stacked widget
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setGeometry(0, 0, 500, 500)

        self.main_page = QWidget()
        self.main_page.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.settings_page = SettingsMenu(parent=self, assets_dir=ASSETS_DIR,
                                          config=self.config)

        # nameplate
        nameplate_l = QLabel(self.main_page)
        nameplate_l.setGeometry(15, 15, 200, 45)
        nameplate_path = ASSETS_DIR / "nameplate.png"
        nameplate = QPixmap(str(nameplate_path))
        nameplate_l.setPixmap(nameplate)
        nameplate_l.setScaledContents(True)

        # song name label
        self.song_name = QLabel(self.main_page)
        self.song_name.setGeometry((18*5), (14*5), (64*5), (4*5))
        song_name_bg_path = (ASSETS_DIR / "song_name_bg.png").as_posix()
        self.song_name.setStyleSheet(f"""
            QLabel {{
                color: #3e2723;
                background-image: url({song_name_bg_path});
                padding-right: 10px;
                padding-left: 10px;
            }}
        """)
        self.song_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_name.setFont(custom_font)

        # artist name label
        self.artist_name = QLabel(self.main_page)
        self.artist_name.setGeometry((60*5), (90*5), (34*5), (4*5))
        artist_name_bg_path = (ASSETS_DIR / "artist_name_bg.png").as_posix()
        self.artist_name.setStyleSheet(f"""
            QLabel {{
                color: #5c4d42;
                background-image: url({artist_name_bg_path});
                padding-right: 10px;
                padding-left: 10px;
            }}
        """)
        self.artist_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artist_name.setFont(custom_font)

        # album cover
        self.album_label = QLabel(self.main_page)
        self.album_label.setGeometry((32*5), (36*5), (38*5), (38*5))
        album_path = ROOT_DIR / "core" / "song_cover.png"
        album_cover = QPixmap(str(album_path))
        self.album_label.setPixmap(album_cover)
        self.album_label.setScaledContents(True)

        # vinyl animation
        vinyl_label = QLabel(self.main_page)
        vinyl_label.setGeometry((16*5), (20*5), 340, 340)
        vinyl_path = ASSETS_DIR / "vinyl.gif"
        self.vinyl = QMovie(str(vinyl_path))
        vinyl_label.setMovie(self.vinyl)
        vinyl_label.setScaledContents(True)
        self.vinyl.start()

        # track the last song title to avoid spamming the discord on play/pause
        self.last_sent_song = ""

        # webhook debounce timer
        self.webhook_timer = QTimer()
        self.webhook_timer.setSingleShot(True)
        self.webhook_timer.setInterval(5000)
        self.webhook_timer.timeout.connect(self.dispatch_webhook)

        self.stacked_widget.addWidget(self.main_page)           # index 0
        self.stacked_widget.addWidget(self.settings_page)       # index 1

        # buttons
        self.closeButton = close_button(self.main_page)
        self.closeButton.clicked.connect(self.hide)     # hide
        self.minimizeButton = minimize_button(self.main_page)
        self.minimizeButton.clicked.connect(self.showMinimized)     # minimize
        self.settingsButton = settings_button(self.main_page)
        self.settingsButton.clicked.connect(self.show_settings_page)    # show settings
        self.previousButton = previous_button(self.main_page)
        self.playPauseButton = play_pause_button(self.main_page)
        self.nextButton = next_button(self.main_page)

        self.settings_page.stng_close_btn.clicked.connect(self.show_main_page)
        self.settings_page.test_discord_btn.clicked.connect(self.send_webhook_test)
        initial_on_top = self.config.get("always_on_top", False)
        self.update_always_on_top(initial_on_top)
        self.settings_page.als_on_top.toggled.connect(self.update_always_on_top)

        # background listeners
        self.listener = SpotifyListener()
        self.listener.song_updated.connect(self.info_update)
        self.listener.start_listener()
        self.previousButton.clicked.connect(self.listener.prev_track)
        self.playPauseButton.clicked.connect(self.listener.toggle_play_pause)
        self.nextButton.clicked.connect(self.listener.next_track)

    def show_settings_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def info_update(self, title, artist, image_bytes, is_playing):
        self.song_name.setText(title)
        self.artist_name.setText(artist)
        
        if image_bytes:
            try:
                new_cover = QPixmap()
                new_cover.loadFromData(image_bytes)
                self.album_label.setPixmap(new_cover)

            # !!! NOT RELEVANT ANYMORE BECAUSE USING MEMORY INSTEAD OF SAVING TO DISK !!!
            # edge case: if win is briefly holding the file open from the bg thread -> catch it
            # eg case - say someone is skipping songs rapidly (maybe 6 or 7 within 2 seconds)
            except PermissionError:
                print(f"thumbnail was locked, skipping this update frame")
            except Exception as e:
                print(f"error loading new cover: {e}")
        else:
            new_cover = QPixmap(str(ASSETS_DIR / "default_cover.png"))  # this pic is transparent
            self.album_label.setPixmap(new_cover)

        # adding '...' if song name too long
        metrics_song = QFontMetrics(self.song_name.font())
        elided_title = metrics_song.elidedText(title, 
                                              Qt.TextElideMode.ElideRight,
                                              self.song_name.width() - 20)    # -20 because padding
        self.song_name.setText(elided_title)

        # adding '...' if artist name too long
        metrics_artist = QFontMetrics(self.artist_name.font())
        elided_name = metrics_artist.elidedText(artist,
                                                Qt.TextElideMode.ElideRight, 
                                                self.artist_name.width() - 20)
        self.artist_name.setText(elided_name)

        self.vinyl.setPaused(not is_playing)

        # play/pause button cahnge
        if is_playing:
            btn_img = (ASSETS_DIR / "btn_pause.png").as_posix()
            btn_pressed_img = (ASSETS_DIR / "btn_pause_pressed.png").as_posix()
        else:
            btn_img = (ASSETS_DIR / "btn_play.png").as_posix()
            btn_pressed_img = (ASSETS_DIR / "btn_play_pressed.png").as_posix()

        self.playPauseButton.setStyleSheet(f"""
            QPushButton {{
                background-image: url({btn_img});
                background-color: transparent;
                border: none;
                padding: 0px;
                margin: 0px;
                outline: none;
            }}
            QPushButton:pressed {{
                background-image: url({btn_pressed_img});
                background-color: transparent;
            }}
        """)

        # discord webhook
        if self.config.get("discord_enabled", False):
            current_song_id = f"{title} - {artist}"
            if current_song_id != self.last_sent_song and is_playing:
                self.pending_webhook_data = (title, artist, image_bytes)
                self.webhook_timer.stop()
                self.webhook_timer.start()
                self.last_sent_song = current_song_id

    def dispatch_webhook(self):
        if self.pending_webhook_data:
            title, artist, image_bytes = self.pending_webhook_data
            send_discord_webhook(
                webhook_url=self.config.get("discord_webhook_url"),
                title=title,
                artist=artist,
                image_bytes=image_bytes,
                icon=self.icon_bytes
            )
            self.pending_webhook_data = None        # clear the pending data

    def send_webhook_test(self):
        url = self.config.get("discord_webhook_url")
        if not url:
            print("No Webhook URL saved")
            return
        
        # placeholder forr test
        send_discord_webhook(
            webhook_url=url,
            title="Test Title",
            artist="Test Artist",
            image_bytes=b"",     # empty byte string as cover
            icon=self.icon_bytes
        )

    def update_always_on_top(self, enabled):
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, enabled)
        self.show()     # refreshing the window

    def toggle_window(self):
        if self.isVisible():
            self.hide()
        else:
            self.showNormal()
            self.activateWindow()

if __name__ == "__main__":
    my_app_id = "spot_vinyl.desktop_widget.v1.0"
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    except AttributeError:
        pass

    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
