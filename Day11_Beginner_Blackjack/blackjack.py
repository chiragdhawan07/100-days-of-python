import random
from art import logo   # ASCII art logo for the game 🎴

# Function to deal a random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 = Ace, 10 covers J/Q/K
    return random.choice(cards)

# Function to calculate the current score
def calculate_score(cards):
    # Check for Blackjack (Ace + 10 as the first two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Adjust Ace value (11 → 1) if score goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Compare user and computer scores to decide the result
def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw! 🤝"
    elif computer_score == 0:
        return "Computer has Blackjack! You lose 😢"
    elif user_score == 0:
        return "You have Blackjack! You win 🎉"
    elif user_score > 21:
        return "You went over 21! You lose 💥"
    elif computer_score > 21:
        return "Computer went over 21! You win 😎"
    elif user_score > computer_score:
        return "You win! 🏆"
    else:
        return "You lose! 😭"

# Main game function
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial 2 cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End if Blackjack or bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask if user wants another card
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Computer's turn: must draw until score ≥ 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

# Keep asking if player wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
