import sys
from PyQt6.QtWidgets import QWidget, QTabBar, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(300, 800)
        self.setWindowTitle("Food Order GUI")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
