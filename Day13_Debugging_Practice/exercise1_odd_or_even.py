# Exercise 1: Odd or Even

# --- Buggy Version ---
def odd_or_even(number):
    if number % 2 = 0: 
        return "This is an even number."
    else:
        return "This is an odd number."


# --- Fixed Version ---
def odd_or_even(number):
    if number % 2 == 0:   # ✅ Corrected comparison operator
        return "This is an even number."
    else:
        return "This is an odd number."


# --- Test Cases ---
print(odd_or_even(3))  # odd
print(odd_or_even(8))  # even
