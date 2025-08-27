class CoffeeMaker:
    """Handles the resources and makes coffee."""

    def __init__(self):
        # Starting stock of the machine
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        # Show what’s left
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        # Check if enough ingredients are available
        for item, amount in drink.ingredients.items():
            if amount > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        # Use ingredients and serve the coffee
        for item, amount in order.ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {order.name} ☕. Enjoy!")
