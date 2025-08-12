# 💰 Day 3 – Treasure Island
# Level: Beginner
# A Python text adventure game where the player's choices decide the outcome.

# Game art (ASCII map)
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[X]
*******************************************************************************''')

# Game introduction
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# First choice: Left or Right
direction = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right':\n").lower()

if direction == "left":
    # Second choice: Wait or Swim
    action = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat or 'swim' to swim across:\n"
    ).lower()

    if action == "wait":
        # Third choice: Door color
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors: red, yellow, blue.\n"
            "Which colour do you choose?\n"
        ).lower()

        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win! 🏆")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif action == "swim":
        print("You were attacked by a trout. Game Over.")
    else:
        print("Invalid choice. Game Over.")

elif direction == "right":
    print("You fell into a hole. Game Over.")

else:
    print("Invalid choice. Game Over.")
