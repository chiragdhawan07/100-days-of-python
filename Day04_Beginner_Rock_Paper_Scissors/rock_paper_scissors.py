import random

print("Welcome to Rock, Paper, Scissors Game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

list_of_images = [rock, paper, scissors]

# Get user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()

print("You chose:")
print(list_of_images[user_choice])

# Get computer choice (as number)
computer_choice = random.randint(0, 2)
print("\nComputer chose:")
print(list_of_images[computer_choice])

# Game logic
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
