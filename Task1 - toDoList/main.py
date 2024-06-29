from PySide6.QtWidgets import QApplication
from myApp import toDoList
import sys

app = QApplication(sys.argv)

window = toDoList()

window.show()
app.exec()