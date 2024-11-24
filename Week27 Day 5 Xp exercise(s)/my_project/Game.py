import random

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        """Ask the user to select rock, paper, or scissors."""
        while True:
            user_choice = input("Please choose rock, paper, or scissors: ").lower()
            if user_choice in self.items:
                return user_choice
            else:
                print("Invalid choice. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        """Select rock, paper, or scissors randomly for the computer."""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """Determine the result of the game."""
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            return 'win'
        else:
            return 'loss'

    def play(self):
        """Play a single round of the game."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You chose {user_item}. The computer chose {computer_item}.", end=" ")

        if result == 'win':
            print("You win!")
        elif result == 'draw':
            print("It's a draw!")
        else:
            print("You lose!")

        return result