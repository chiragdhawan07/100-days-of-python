from art import logo   # Importing the ASCII logo art
import os                  # Importing os module to clear the console screen

# Print the logo at the start of the program
print(logo)


# Function to clear the console screen
def clear():
    # 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to find the highest bidder from all bids
def find_highest_bidder(bidding_record):
    highest_bid = 0        # Keeps track of the highest bid so far
    winner = ""            # Stores the name of the person with the highest bid
    
    # Loop through each bidder in the dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        # If this bidder placed a higher bid than the current highest
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    # Print the winner at the end
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Dictionary to store all bids: {name: bid}
bids = {}

# Boolean flag to control the bidding loop
continue_bidding = True

# Main bidding loop
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price   # Save the bid in dictionary
    
    # Ask if more bidders are left
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if should_continue == "no":
        continue_bidding = False       # Stop the loop
        find_highest_bidder(bids)      # Find and print the winner
    elif should_continue == "yes":
        clear()                        # Clear screen to hide previous bids
