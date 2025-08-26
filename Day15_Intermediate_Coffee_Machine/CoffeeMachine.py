# -------------------- Coffee Machine Project --------------------

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# -------------------- MACHINE RESOURCES --------------------
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# -------------------- FUNCTIONS --------------------
def is_resource_sufficient(order_ingredients):
    """Returns True if there are enough resources, otherwise False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Prompts user to insert coins and returns the total amount inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    """Checks if the user inserted enough money.
    If yes → add profit, return True.
    If no → refund money, return False.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change.\nProcessing your order....")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Refund successful!")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts required ingredients from resources and serves the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# -------------------- MAIN PROGRAM LOOP --------------------
is_machine_on = True

while is_machine_on:
    # Get user choice
    user_choice = input("What would you like to have? (espresso/latte/cappuccino): ").strip().lower()

    if user_choice == "off":
        # Shut down the coffee machine
        print("Goodbye!")
        is_machine_on = False

    elif user_choice == "report":
        # Show current resources and profit
        resources_left = (
            f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${profit}"
        )
        print(resources_left)

    elif user_choice in MENU:
        # Process drink order
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])

    else:
        # Invalid entry
        print("Invalid choice. Please try again.")
