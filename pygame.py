import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Try again.")
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

# Play the game
play_game()
