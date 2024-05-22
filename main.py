import sys
from PyQt6.QtWidgets import QWidget, QTabBar, QApplication
from PizzaTab import PizzaTab

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """MainWindow widget setup"""
        self.setMinimumSize(300, 800)
        self.setWindowTitle("Food Order GUI")
        self.setUpMainWindow()
        self.show() #


    def mainGridLayout(self):
        """Main grid layout for MainWindow widget"""
        



    def setUpMainWindow(self):
        pizza_tab_v_box = PizzaTab()
        self.setLayout(pizza_tab_v_box.mainLayout())
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
