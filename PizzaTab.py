import sys
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QRadioButton,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QButtonGroup,
    QGroupBox,
)
from PyQt6.QtGui import QPixmap
from pizza_data import toppings, crusts
from PyQt6.QtCore import QMargins
from styles import styles


class PizzaTab(QWidget):
    def __init__(self):
        super().__init__()

    def buildPizzaLayout(self):
        """Vertical layout for build pizza portion of application"""
        build_pizza_v_box = QVBoxLayout()
        build_pizza_h_box = QHBoxLayout()

        build_pizza_label = QLabel("BUILD YOUR OWN PIZZA")
        pizza_img = QLabel()
        pizza_img.setPixmap(QPixmap("images\pizza.png"))
        pizza_img.setScaledContents(True)
        pizza_img.setFixedSize(100, 100)
        pizza_img.setObjectName("PizzaImage")

        pizza_info = QLabel(
            "Build a custom pizza for you. Start with your favorite crust and add any toppings, plus the perfect amount of cheese and sauce"
        )
        pizza_info.setWordWrap(True)
        pizza_info.setContentsMargins(QMargins(10, 10, 10, 10))

        pizza_info.setObjectName("PizzaInfo")

        build_pizza_h_box.addWidget(pizza_img)
        build_pizza_h_box.addWidget(pizza_info)
        build_pizza_v_box.addWidget(build_pizza_label)
        build_pizza_v_box.addLayout(build_pizza_h_box)

        return build_pizza_v_box

    def chooseCrustLayout(self):
        """Vertical layout for choose curst portion of applcation"""
        crust_v_box = QVBoxLayout()

        crust_gb = QGroupBox("CHOOSE YOUR CRUST")

        # choose_crust_label = QLabel("CHOOSE YOUR CRUST")
        # choose_crust_label.setObjectName("Crust_Label")

        # choose_crust_v_box.addWidget(choose_crust_label)

        for crust in crusts:
            crust_rb = QRadioButton(crust)
            
            crust_v_box.addWidget(crust_rb)


        crust_gb.setLayout(crust_v_box)

        return crust_gb

    def chooseToppingsLayout(self):
        """Vertical layout for choose topping portion of application"""
        topping_v_box = QVBoxLayout()
        topping_gb = QGroupBox("CHOOSE YOUR TOPPINGS")
        # topping_rb_group = QButtonGroup()

        # choose_topping_label = QLabel("CHOOSE YOUR TOPPINGS")

        # topping_v_box.addWidget(choose_topping_label)

        for topping in toppings:
            topping_rb = QRadioButton(topping)
            topping_rb.setAutoExclusive(False)

            # topping_rb_group.addButton(topping_rb)
            topping_v_box.addWidget(topping_rb)

        topping_gb.setLayout(topping_v_box)

        return topping_gb

    # Might switch to QGridBox() layout
    def mainLayout(self):
        """Main Layout for PizzaTab widget"""
        main_v_box = QVBoxLayout()

        self.setStyleSheet(styles)

        main_v_box.addLayout(self.buildPizzaLayout())
        main_v_box.addWidget(self.chooseCrustLayout())
        main_v_box.addWidget(self.chooseToppingsLayout())

        return main_v_box
