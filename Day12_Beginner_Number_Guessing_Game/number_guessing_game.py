# Number Guessing Game 🎲

import random

# Game Constants
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def welcome_message():
    """Display welcome text and rules."""

    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Your goal is to guess it in as few attempts as possible.\n")

def choose_difficulty():
    """
    Ask the user to select difficulty level.
    Easy = 10 attempts, Hard = 5 attempts.
    Keeps asking until valid input is given.
    """

    while True:
        choice = input("Choose a difficulty (easy/hard): ").lower()
        if choice == "easy":
            return EASY_ATTEMPTS
        elif choice == "hard":
            return HARD_ATTEMPTS
        else:
            print("❌ Invalid input! Please type 'easy' or 'hard'.")

def get_guess():
    """Get a valid integer guess from the player."""

    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")

def check_guess(guess, answer, attempts_left):
    """
    Compare guess to answer and return updated attempts.
    Also prints feedback (too high / too low).
    """

    if guess > answer:
        print("📈 Too high.")
        return attempts_left - 1
    elif guess < answer:
        print("📉 Too low.")
        return attempts_left - 1
    else:
        print(f"🎯 Correct! The answer was {answer}. You win! 🎉")
        return -1   # Special flag to indicate correct guess

def play_game():
    """Main game loop."""

    welcome_message()
    answer = random.randint(1, 100)   # Computer chooses the number
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        guess = get_guess()

        attempts = check_guess(guess, answer, attempts)

        if attempts == -1:  # Player guessed correctly
            return
        elif attempts == 0:
            print(f"💀 You've run out of guesses! The number was {answer}.")

# Run the game
play_game()
