from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout


class YourOrder(QWidget):
    def __init__(self):
        super().__init__()

    def orderDetailsLayout(self) -> QGridLayout:
        order_details_g_box = QGridLayout()

        pizza_type_label = QLabel("Pizza Type: ")
        pizza_type_details_label = QLabel("Hand-tossed")

        toppings_label = QLabel("Toppings: ")
        toppings_details_label = QLabel("Pepperoni\nSausage\nPineapple\nCheese\n")

        extra_label = QLabel("Extra: ")
        extra_details_label = QLabel("Sweet-sour Wings")

        order_details_g_box.addWidget(pizza_type_label, 0, 0)
        order_details_g_box.addWidget(pizza_type_details_label, 0, 1)
        order_details_g_box.addWidget(toppings_label, 1, 0)
        order_details_g_box.addWidget(toppings_details_label, 1, 1)
        order_details_g_box.addWidget(extra_label, 2, 0)
        order_details_g_box.addWidget(extra_details_label, 2, 1)

        return order_details_g_box

    def mainLayout(self) -> QVBoxLayout:
        """Main vertical layout for YourOrder widget"""
        main_v_box = QVBoxLayout()

        main_v_box.addLayout(self.orderDetailsLayout())

        return main_v_box
