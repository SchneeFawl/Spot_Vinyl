# boilerplate buttons code

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = PROJECT_DIR / "assets"

def close_button(parent) -> QPushButton:
    btn_close_img = (ASSET_DIR / "btn_close.png").as_posix()
    btn_close_pressed_img = (ASSET_DIR / "btn_close_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
    button.setGeometry((88*5), (2*5), 50, 55)

    # niche but when the spacebar is pressed after the button is clicked via mouse,
    # it registers it as a button press
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

def minimize_button(parent) -> QPushButton:
    btn_img = (ASSET_DIR / "btn_minimize.png").as_posix()
    btn_pressed_img = (ASSET_DIR / "btn_minimize_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
            background-color: transparent
        }}
    """)
    button.setGeometry((76*5), (2*5), 50, 55)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

def settings_button(parent) -> QPushButton:
    btn_img = (ASSET_DIR / "btn_settings.png").as_posix()
    btn_pressed_img = (ASSET_DIR / "btn_settings_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
    button.setGeometry((64*5), (2*5), 50, 55)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

def previous_button(parent) -> QPushButton:
    btn_img = (ASSET_DIR / "btn_previous.png").as_posix()
    btn_pressed_img = (ASSET_DIR / "btn_previous_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
    button.setGeometry((2*5), (87*5), 50, 55)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

def play_pause_button(parent) -> QPushButton:
    btn_img = (ASSET_DIR / "btn_pause.png").as_posix()
    btn_pressed_img = (ASSET_DIR / "btn_pause_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
    button.setGeometry((14*5), (87*5), 50, 55)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

def next_button(parent) -> QPushButton:
    btn_img = (ASSET_DIR / "btn_next.png").as_posix()
    btn_pressed_img = (ASSET_DIR / "btn_next_pressed.png").as_posix()
    button = QPushButton(parent)
    button.setStyleSheet(f"""
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
    button.setGeometry((26*5), (87*5), 50, 55)
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    return button

'''
def stng_close_button(parent) -> QPushButton:
    button = QPushButton()
    button_close_img = (ASSET_DIR / "btn_close.png").as_posix() # type: ignore
    button_close_pressed_img = (ASSET_DIR / "btn_close_pressed.png").as_posix() # type: ignore
    button.setStyleSheet(f"""
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
    button.setGeometry((85*5), (5*5), (10*5), (11*5))
    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    
    return button
'''
