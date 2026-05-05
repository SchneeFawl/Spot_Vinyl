import sys
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

# root directory for the project
ROOT_DIR = Path(__file__).resolve().parent.parent
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

        self.closeButton()

    def closeButton(self):
        btn_close_img = (ASSETS_DIR / "btn_close.png").as_posix()
        btn_close_pressed_img = (ASSETS_DIR / "btn_close_pressed.png").as_posix()
        btn_close = QPushButton(self)
        btn_close.setStyleSheet(f"""
            QPushButton {{
                background-image: url({btn_close_img});
                background-color: transparent;

                /* for some reasons there is hidden padding and borders */
                border: none;
                padding: 0px;
                margin: 0px;
                outline: none;
            }}
            QPushButton:pressed {{
                background-image: url({btn_close_pressed_img});
                background-color: transparent
            }}
        """)
        # btn_close.move(440, 10)
        # btn_close.setFixedSize(50, 55)
        btn_close.setGeometry((88*5), 10, 50, 55)

        # very niche but when the spacebar is pressed after the button is clicked via mouse,
        # it registers it as a button press
        btn_close.setFocusPolicy(Qt.FocusPolicy.NoFocus)


app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())
