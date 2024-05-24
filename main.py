import sys
from PyQt6.QtWidgets import QWidget, QTabBar, QApplication, QGridLayout
from PizzaTab import PizzaTab
from YourOrder import YourOrder

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


    def mainGridLayout(self) -> QGridLayout:
        """Main grid layout for MainWindow widget"""
        main_g_box = QGridLayout()
        pizza_tab_v_box = PizzaTab()
        your_order_v_box = YourOrder()

        main_g_box.addLayout(pizza_tab_v_box.mainLayout(), 0, 0)
        main_g_box.addLayout(your_order_v_box.mainLayout(), 0, 1)

        return main_g_box
        



    def setUpMainWindow(self):
        pizza_tab_v_box = PizzaTab()
        self.setLayout(self.mainGridLayout())
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
