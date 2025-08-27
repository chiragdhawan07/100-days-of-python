class MoneyMachine:
    """Handles money transactions for the coffee machine."""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Takes coin input from the user and returns the total amount."""
        print("Please insert coins.")
        total = 0
        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}?: "))
            total += count * self.COIN_VALUES[coin]
        return total

    def make_payment(self, cost):
        """Returns True if payment is successful, False if not."""
        self.money_received = self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that’s not enough money. Money refunded.")
            self.money_received = 0
            return False
