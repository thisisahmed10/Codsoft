import random
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)

class RockPaperScissors(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rock Paper Scissors")

        self.user_choice_label = QLabel("Your Choice:")
        self.user_choice_display = QLabel("...")
        self.computer_choice_label = QLabel("Computer's Choice:")
        self.computer_choice_display = QLabel("...")
        self.result_label = QLabel("...")

        self.rock_button = QPushButton("Rock")
        self.rock_button.clicked.connect(lambda: self.play("rock"))
        self.paper_button = QPushButton("Paper")
        self.paper_button.clicked.connect(lambda: self.play("paper"))
        self.scissors_button = QPushButton("Scissors")
        self.scissors_button.clicked.connect(lambda: self.play("scissors"))

        self.play_again_button = QPushButton("Play Again")
        self.play_again_button.setEnabled(False)
        self.play_again_button.clicked.connect(self.reset_game)

        # Layout
        choice_layout = QHBoxLayout()
        choice_layout.addWidget(self.rock_button)
        choice_layout.addWidget(self.paper_button)
        choice_layout.addWidget(self.scissors_button)

        info_layout = QVBoxLayout()
        info_layout.addWidget(self.user_choice_label)
        info_layout.addWidget(self.user_choice_display)
        info_layout.addWidget(self.computer_choice_label)
        info_layout.addWidget(self.computer_choice_display)
        info_layout.addWidget(self.result_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(info_layout)
        main_layout.addLayout(choice_layout)
        main_layout.addWidget(self.play_again_button)

        self.setLayout(main_layout)

        self.user_score = 0
        self.computer_score = 0
        self.show()

    def play(self, user_choice):
        self.user_choice_display.setText(user_choice)
        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.computer_choice_display.setText(computer_choice)

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "paper" and computer_choice == "rock"
        ) or (user_choice == "scissors" and computer_choice == "paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        self.result_label.setText(result)

        # Play again:
        self.play_again_button.setEnabled(True)
    # Reset the game:
    def reset_game(self):
        self.user_choice_display.setText("...")
        self.computer_choice_display.setText("...")
        self.result_label.setText("")
        self.play_again_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication([])
    game = RockPaperScissors()
    app.exec()
