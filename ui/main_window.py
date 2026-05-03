import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spot_Vinyl")
        self.setFixedSize(500, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # removes title bar
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)    # for transparency

        # the main background image
        BG_LABEL = QLabel(self)
        BG_LABEL.setGeometry(0, 0, 500, 500)
        BACKGROUND = QPixmap("D:/Coding/Spot_Vinyl/assets/bg_main.png")
        BG_LABEL.setPixmap(BACKGROUND)
        BG_LABEL.setScaledContents(True)


app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())
