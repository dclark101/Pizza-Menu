import sys
from PyQt6.QtWidgets import (
    QWidget,
    QTabBar,
    QApplication,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QGroupBox
)
from PyQt6.QtCore import Qt
from PizzaTab import PizzaTab
from YourOrder import YourOrder
from styles import styles


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """MainWindow widget setup"""
        self.setMinimumSize(700, 700)
        self.setWindowTitle("Food Order GUI")
        self.setUpMainWindow()
        self.show()  #

    def mainGridLayout(self) -> QGridLayout:
        """Main grid layout for MainWindow widget"""
        self.main_g_box = QGridLayout()
        self.main_v_box = QVBoxLayout()
        pizza_tab_v_box = PizzaTab().mainLayout()
        your_order_v_box = YourOrder()
        add_to_order_btn = QPushButton("Add To Order")
        add_to_order_btn.setMinimumWidth(20)

        self.main_v_box.setContentsMargins(20, 20, 20, 20)

        main_tab = QTabBar()
        main_tab.addTab("Pizza")
        main_tab.addTab("Wings")

        self.main_v_box.addWidget(main_tab)
        self.main_v_box.addLayout(pizza_tab_v_box)
        self.main_v_box.addWidget(add_to_order_btn)

        # self.main_g_box.addWidget(main_tab, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        self.main_g_box.addLayout(self.main_v_box, 0, 0)
        self.main_g_box.addLayout(your_order_v_box.mainLayout(), 0, 1)

        return self.main_g_box

    def setUpMainWindow(self):
        pizza_tab_v_box = PizzaTab()

        self.setLayout(self.mainGridLayout())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(styles)
    window = MainWindow()

    sys.exit(app.exec())
