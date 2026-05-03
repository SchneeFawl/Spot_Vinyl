from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spot_Vinyl")
        self.setFixedSize(500, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)      # removes title bar
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)       # for transparency


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
