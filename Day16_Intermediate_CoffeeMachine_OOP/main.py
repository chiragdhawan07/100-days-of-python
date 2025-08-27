# Coffee Machine (OOP Version) – Main Program

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Machine components
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower().strip()

    if choice == "off":
        print("Turning off... Goodbye! 👋")
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)  # returns None if not found
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
