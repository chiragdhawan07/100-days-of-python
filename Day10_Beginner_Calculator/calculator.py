import os
from art import logo   # ASCII art logo file (make sure art.py is in the same folder)

# Print the calculator logo on start
print(logo)

def clear():
    """Clear the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ------------------- Calculator Operations ------------------- #
def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Return the quotient of two numbers, handle division by zero."""
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

# Dictionary to map symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# ------------------- Main Calculator Function ------------------- #
def calculator():
    """Runs the calculator program with options to continue, restart, or quit."""
    num1 = float(input("What is your first number?: "))

    while True:
        # Show available operations
        for symbol in operations:
            print(symbol)
        
        # Ask user to pick operation
        operation = input("Pick an operation: ")
        num2 = float(input("What is your next number?: "))

        # Perform calculation
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        # Ask user what to do next
        choice = input(
            f"Type 'y' to continue with {answer}, "
            f"'n' to start a new calculation, "
            f"or 'q' to quit: "
        )

        if choice == "y":
            # Continue with previous answer
            num1 = answer
        elif choice == "n":
            # Restart calculator fresh
            clear()
            calculator()
            break
        else:
            # Exit program
            print("Goodbye! 👋")
            break

# ------------------- Program Entry Point ------------------- #
calculator()
