import random
import os
from game_data import data
from artday14 import logo, vs

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Format account details into printable string
def format_account(account):
    """Return account data as a formatted string."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

# Compare follower counts
def compare(guess, a_followers, b_followers):
    """Check if user guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Game function
def game():
    print(logo)
    score = 0
    game_should_continue = True
    
    account_a = random.choice(data)
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b  # move B → A
        account_b = random.choice(data)
        
        # Ensure A and B are not the same
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"\nCompare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']

        is_correct = compare(guess, a_followers, b_followers)

        clear()
        print(logo)
        
        if is_correct:
            score += 1
            print(f"✅ Correct! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"❌ Wrong! Final score: {score}")

# Run the game
game()
