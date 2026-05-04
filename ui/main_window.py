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
        # btn_close_l.setGeometry((88*5), 10, 50, 55)
        btn_close_img = ASSETS_DIR / "btn_close.png"
        btn_close_img_dir = btn_close_img.as_uri()
        btn_close = QPushButton()
        btn_close.setStyleSheet(f"background-image: url({btn_close_img_dir})")
        '''
        btn_close.setStyleSheet(f"""
            QPushButton {{
                background-image: url("{btn_close_img_dir}");
            }}
        """)
        '''
        btn_close.setGeometry(440, 10, 50, 55)



app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())
