class MenuItem:
    # Represents one drink
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    # Holds all available drinks
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_items(self):
        # Return names like "latte/espresso/cappuccino"
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        # Search and return drink object if found
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")
        return None
