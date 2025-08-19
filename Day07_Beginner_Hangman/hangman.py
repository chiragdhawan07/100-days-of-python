import random

from hangman_words import word_list
from hangman_art import stages, logo

# Starting lives
lives = 6

# Print game logo
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)

# Create placeholder for the hidden word (e.g., "____")
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Game state variables
game_over = False
correct_letters = []  # Stores correctly guessed letters

# Main game loop
while not game_over:

    # Show lives left
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    # Ask player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""  # Build the updated word display

    # Reveal guessed letters in the word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)  # Add correct letter to the list
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If guessed letter is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # Game over if no lives left
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check if word is fully guessed
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print hangman stage art
    print(stages[lives])
