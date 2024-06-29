import sys
from random import choices
from string import ascii_letters, digits, punctuation
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QLineEdit,
)


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.length_section = QHBoxLayout()
        self.layout.addLayout(self.length_section)

        self.length_label = QLabel("Password Length:")
        self.length_section.addWidget(self.length_label)

        self.length_spinbox = QSpinBox()
        self.length_spinbox.setMinimum(8)
        self.length_spinbox.setValue(16)
        self.length_section.addWidget(self.length_spinbox)

        # Character options:
        self.options_section = QVBoxLayout()
        self.layout.addLayout(self.options_section)

        self.include_uppercase = QCheckBox("Include Uppercase Letters")
        self.include_uppercase.setChecked(True)
        self.options_section.addWidget(self.include_uppercase)

        self.include_lowercase = QCheckBox("Include Lowercase Letters")
        self.include_lowercase.setChecked(True)
        self.options_section.addWidget(self.include_lowercase)

        self.include_digits = QCheckBox("Include Digits")
        self.include_digits.setChecked(True)
        self.options_section.addWidget(self.include_digits)

        self.include_symbols = QCheckBox("Include Symbols")
        self.include_symbols.setChecked(True)
        self.options_section.addWidget(self.include_symbols)

        # Generate button and password display
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.layout.addWidget(self.password_display)

    def generate_password(self):
        # User options:
        length = self.length_spinbox.value()
        include_uppercase = self.include_uppercase.isChecked()
        include_lowercase = self.include_lowercase.isChecked()
        include_digits = self.include_digits.isChecked()
        include_symbols = self.include_symbols.isChecked()

        char_pool = ""
        if include_uppercase:
            char_pool += ascii_letters.upper()
        if include_lowercase:
            char_pool += ascii_letters.lower()
        if include_digits:
            char_pool += digits
        if include_symbols:
            char_pool += punctuation

        # Generate and display password:
        password = "".join(choices(char_pool, k=length))
        self.password_display.setText(password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    password_generator = PasswordGenerator()
    password_generator.show()
    sys.exit(app.exec_())
