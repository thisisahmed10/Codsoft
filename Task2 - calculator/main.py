from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSizePolicy

# Calculator class:
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.expression = ""
        self.layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        button_data = {
            (1, 0): "7", (1, 1): "8", (1, 2): "9", (1, 3): "divide",
            (2, 0): "4", (2, 1): "5", (2, 2): "6", (2, 3): "multiply",
            (3, 0): "1", (3, 1): "2", (3, 2): "3", (3, 3): "minus",
            (4, 0): "0", (4, 1): "dot", (4, 2): "equal", (4, 3): "plus",
            (5, 0): "C",
        }

        for (row, col), text in button_data.items():
            button = QPushButton(text)
            button.clicked.connect(getattr(self, f"button_{text}"))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.layout.addWidget(button, row, col)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Calculator")

    # Buttons functions:
    def button_0(self):
        self.expression += "0"
        self.display.setText(self.expression)

    def button_1(self):
        self.expression += "1"
        self.display.setText(self.expression)

    def button_2(self):
        self.expression += "2"
        self.display.setText(self.expression)

    def button_3(self):
        self.expression += "3"
        self.display.setText(self.expression)

    def button_4(self):
        self.expression += "4"
        self.display.setText(self.expression)

    def button_5(self):
        self.expression += "5"
        self.display.setText(self.expression)

    def button_6(self):
        self.expression += "6"
        self.display.setText(self.expression)

    def button_7(self):
        self.expression += "7"
        self.display.setText(self.expression)

    def button_8(self):
        self.expression += "8"
        self.display.setText(self.expression)

    def button_9(self):
        self.expression += "9"
        self.display.setText(self.expression)

    def button_dot(self):
        self.expression += "."
        self.display.setText(self.expression)

    def button_plus(self):
        self.expression += "+"
        self.display.setText(self.expression)

    def button_minus(self):
        self.expression += "-"
        self.display.setText(self.expression)

    def button_multiply(self):
        self.expression += "*"
        self.display.setText(self.expression)

    def button_divide(self):
        self.expression += "/"
        self.display.setText(self.expression)

    def button_C(self):
        self.expression = ""
        self.display.setText(self.expression)

    def button_equal(self):
        try:
            result = eval(self.expression)
            self.display.setText(str(result))
            self.expression = str(result)
        except Exception as e:
            self.display.setText("Error")
            self.expression = ""

app = QApplication([])
calculator = Calculator()
calculator.show()
app.exec()
