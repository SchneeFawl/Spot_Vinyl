from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
# assets_dir = root_dir / "assets"

class SettingsMenu(QWidget):
    def __init__(self, parent = None, assets_dir = None):
        super().__init__(parent)

        self.setFixedSize(500, 500)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 500, 500)
        bg_path = (assets_dir / "settings_menu.png") # type: ignore
        bg_img = QPixmap(str(bg_path))
        self.bg_label.setPixmap(bg_img)
        self.bg_label.setScaledContents(True)

        
        self.stng_close_btn = QPushButton(self)
        button_close_img = (assets_dir / "btn_close.png").as_posix() # type: ignore
        button_close_pressed_img = (assets_dir / "btn_close_pressed.png").as_posix() # type: ignore
        self.stng_close_btn.setStyleSheet(f"""
            QPushButton {{
                background-image: url({button_close_img});
                background-color: transparent;
                padding: 0px;
                border: none;
                margin: 0px;
                outline: none;
            }}
            QPushButton:pressed {{
                background-image: url({button_close_pressed_img});
                background-color: transparent;
            }}
        """)
        self.stng_close_btn.setGeometry((85*5), (5*5), (10*5), (11*5))
        
