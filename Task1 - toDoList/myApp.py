from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLineEdit,
    QPushButton,
)

class toDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.resize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Task list
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        self.task_list.itemSelectionChanged.connect(self.get_selected_task)

        self.input_section = QHBoxLayout()
        self.layout.addLayout(self.input_section)

        # Input task
        self.task_input = QLineEdit()
        self.input_section.addWidget(self.task_input)

        # Add task
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.input_section.addWidget(self.add_button)

        # Delete task
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_button.setEnabled(False)  # Disable initially
        self.input_section.addWidget(self.delete_button)
        self.tasks = []

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.setText("")

    def get_selected_task(self):
        self.delete_button.setEnabled(len(self.task_list.selectedItems()) > 0)

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                row = self.task_list.row(item)
                del self.tasks[row]
                self.task_list.takeItem(row)