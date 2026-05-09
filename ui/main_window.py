import sys
from pathlib import Path
# root directory for the project
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtWidgets import \
    QApplication, QMainWindow, QLabel
from buttons import *
from core.song import SpotifyListener


ASSETS_DIR = ROOT_DIR / "assets"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spot_Vinyl")
        self.setFixedSize(500, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)    # for transparent bg

        # the main background image
        BG_LABEL = QLabel(self)
        BG_LABEL.setGeometry(0, 0, 500, 500)
        bg_path = ASSETS_DIR / "bg_main.png"
        BACKGROUND = QPixmap(str(bg_path))
        BG_LABEL.setPixmap(BACKGROUND)
        BG_LABEL.setScaledContents(True)

        # nameplate
        nameplate_l = QLabel(self)
        nameplate_l.setGeometry(15, 15, 200, 45)
        nameplate_path = ASSETS_DIR / "nameplate.png"
        nameplate = QPixmap(str(nameplate_path))
        nameplate_l.setPixmap(nameplate)
        nameplate_l.setScaledContents(True)

        # song name label
        self.song_name = QLabel("sixty seven" ,self)
        self.song_name.setGeometry((25*5), (14*5), (50*5), (4*5))
        self.song_name.setStyleSheet(f"""
            QLabel {{
                color: #FFF0BE;
                font-weight: bold;
                font-size: 17px;
            }}
        """)

        # artist name label
        self.artist_name = QLabel("Epic Artist", self)
        self.artist_name.setGeometry((60*5), (90*5), (50*5), (4*5))
        self.artist_name.setStyleSheet(f"""
            QLabel {{
                color: #FFF0BE;
                font-weight: bold;
                font-size: 17px;
            }}
        """)

        # album cover
        self.album_label = QLabel(self)
        self.album_label.setGeometry((32*5), (36*5), (38*5), (38*5))
        album_path = ROOT_DIR / "core" / "song_cover.png"
        album_cover = QPixmap(str(album_path))
        self.album_label.setPixmap(album_cover)
        self.album_label.setScaledContents(True)

        # vinyl animation
        vinyl_label = QLabel(self)
        vinyl_label.setGeometry((16*5), (20*5), 340, 340)
        vinyl_path = ASSETS_DIR / "vinyl.gif"
        vinyl = QMovie(str(vinyl_path))
        vinyl_label.setMovie(vinyl)
        vinyl_label.setScaledContents(True)
        vinyl.start()

        # buttons
        self.closeButton = minimize_button(self)
        self.minimizeButton = close_button(self)
        self.settingsButton = settings_button(self)
        self.previousButton = previous_button(self)
        self.pauseButton = pause_button(self)
        self.nextButton = next_button(self)

        # background listeners
        self.listener = SpotifyListener()
        self.listener.song_updated.connect(self.info_update)
        self.listener.start_listener()

    def info_update(self, title, artist, image_bytes):
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

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
