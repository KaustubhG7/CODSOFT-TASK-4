import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors Game")
        self.master.geometry("400x300")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Welcome to Rock, Paper, Scissors!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(master, text="Choose your option to start the game", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"), width=10, height=2)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"), width=10, height=2, )
        # self.paper_button.pack()
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"), width=10, height=2)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, width=10, height=2)
        self.play_again_button.pack(side=tk.RIGHT, pady=20, padx=10)

    def get_computer_choice(self):
        """Randomly select rock, paper, or scissors for the computer."""
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner based on user and computer choices."""
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def play(self, user_choice):
        """Play a round of the game."""
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def reset_game(self):
        """Reset the game scores."""
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0, Computer: 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()