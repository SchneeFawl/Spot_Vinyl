from PyQt6.QtWidgets import \
    QWidget, QLabel, QPushButton, QLineEdit, QCheckBox, QComboBox
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

        # bg
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 500, 500)
        bg_path = (assets_dir / "settings_menu.png") # type: ignore
        bg_img = QPixmap(str(bg_path))
        self.bg_label.setPixmap(bg_img)
        self.bg_label.setScaledContents(True)

        # close button (settings)
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

        self.webhook_input = QLineEdit(self)
        self.webhook_input.setPlaceholderText("Paste Discord Webhook URL here")
        self.webhook_input.setGeometry((5*10), (20*5), (72*5), (8*5))

        self.als_on_top = QCheckBox("Always on top", self)
        self.als_on_top.setGeometry((10*5),(32*5), (40*5), (10*5))
        als_on_top_img = (assets_dir / "on_top_checkbox.png").as_posix()   # type: ignore
        als_on_top_checked_img = (assets_dir / "on_top_checkbox_checked.png").as_posix()   # type: ignore
        self.als_on_top.setStyleSheet(f"""
            QCheckBox::indicator {{
                width: 50px;
                height: 50px;
            }}
            QCheckBox::indicator:unchecked {{
                image: url({als_on_top_img})
                padding: 0px;
            }}
            QCheckBox::indicator:checked {{
                background-image: url({als_on_top_checked_img});
                padding: 0px;
            }}
        """)

        self.theme_label = QLabel("Select theme:", self)
        self.theme_label.setGeometry((10*5), (46*5), (20*5), (6*5))
        self.theme_dropdown = QComboBox(self)
        self.theme_dropdown.addItems(["Classic", "Space"])  # placeholder themes
        self.theme_dropdown.setGeometry((10*5), (52*5), (40*5), (8*5))  # 48, 

        self.test_discord_btn = QPushButton("Test Discord webhook", self)
        self.test_discord_btn.setGeometry((10*5), (64*5), (40*5), (9*5))
