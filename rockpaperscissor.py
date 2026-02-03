import random

# Constants
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# Map choices to emojis (you can change emojis as you like)
emojis = {
    ROCK: "🪨",
    PAPER: "📄",
    SCISSORS: "✂️",
}

# Choices tuple derived from keys of the dictionary (DRY)
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissors? (r/p/s): ").strip().lower()

        if user_choice in choices:
            return user_choice

        print("Invalid choice, please enter 'r', 'p', or 's'.")


def get_computer_choice():
    return random.choice(choices)


def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie.")
        return

    if (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win!")
    else:
        print("You lose.")


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input("Do you want to continue? (y/n): ").strip().lower()
        if should_continue == "n":
            break


if __name__ == "__main__":
    play_game()
