from game import Game

def get_user_menu_choice():
    """Display the menu and get the user's choice."""
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    while True:
        choice = input("Choose an option (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def print_results(results):
    """Print the results of the games played."""
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    """Main function to control the flow of the game."""
    results = {'win': 0, 'loss': 0, 'draw': 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':  # Play a new game
            game = Game()
            result = game.play()

            # Update the results based on the game result
            if result == 'win':
                results['win'] += 1
            elif result == 'loss':
                results['loss'] += 1
            else:
                results['draw'] += 1
        
        elif choice == '2':  # Show scores
            print_results(results)
        
        elif choice == '3':  # Quit the game
            print_results(results)
            print("Goodbye!")
            break