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
        webhook_input_img = (assets_dir / "webhook_box.png").as_posix()    # type: ignore
        self.webhook_input.setStyleSheet(f"""
            QLineEdit {{
                background-image: url({webhook_input_img});
                background-color: transparent;
                border: none;
                padding: 10px;
                margin: 0px;
                outline: none;
            }}
        """)

        self.als_on_top = QCheckBox("", self)
        # self.als_on_top.setGeometry((10*5),(32*5), (40*5), (10*5))
        self.als_on_top.setGeometry((10*5),(32*5), (50), (10*5))
        als_on_top_img = (assets_dir / "on_top_checkbox.png").as_posix()   # type: ignore
        als_on_top_checked_img = (assets_dir / "on_top_checkbox_checked.png").as_posix()   # type: ignore
        self.als_on_top.setStyleSheet(f"""
            QCheckBox::indicator {{
                width: 50px;
                height: 50px;
            }}
            QCheckBox::indicator:unchecked {{
                image: url({als_on_top_img});
            }}
            QCheckBox::indicator:checked {{
                background-image: url({als_on_top_checked_img});
            }}
        """)

        self.theme_label = QLabel("Select theme:", self)
        self.theme_label.setGeometry((10*5), (46*5), (20*5), (6*5))

        self.theme_dropdown = QComboBox(self)
        self.theme_dropdown.addItems(["Classic", "Space"])  # placeholder themes
        self.theme_dropdown.setGeometry((10*5), (52*5), (40*5), (8*5))
        theme_dropdown_img = (assets_dir / "theme_combobox.png").as_posix() # type: ignore
        theme_dropdown_arrow_img = (assets_dir / "theme_combobox_arrow.png").as_posix() # type: ignore
        theme_dropdown_list_img = (assets_dir / "theme_combobox_list.png").as_posix() # type: ignore
        self.theme_dropdown.setStyleSheet(f"""
            QComboBox {{
                border-image: url({theme_dropdown_img}) 0 0 0 0;
                padding: 10px;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 40px;
            }}
            QComboBox::down-arrow {{
                image: url({theme_dropdown_arrow_img});
                width: 24px;
                height: 24px;
            }}
            QComboBox QAbstractItemView {{
                border-image: url({theme_dropdown_list_img}) 0 5 5 5;
                border-width: 0px 5px 5px 5px;
                background-color: #e5d5e7;
                selection-background-color: #ffa3af;
            }}
        """)

        self.test_discord_btn = QPushButton("Test Discord webhook", self)
        self.test_discord_btn.setGeometry((10*5), (66*5), (40*5), (9*5))
        test_discord_img = (assets_dir / "btn_webhook_test.png").as_posix() # type: ignore
        test_discord_pressed_img = (assets_dir / "btn_webhook_test_pressed.png").as_posix() # type: ignore
        self.test_discord_btn.setStyleSheet(f"""
            QPushButton {{
                background-image: url({test_discord_img});
                background-color: transparent;
                padding: 0px;
                border: none;
                margin: 0px;
                outline: none;
            }}
            QPushButton::pressed {{
                background-image: url({test_discord_pressed_img});
                background-color: transparent;
            }}
        """)

        
