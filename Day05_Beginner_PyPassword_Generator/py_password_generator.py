import random

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']

print("Welcome to the PyPassword Generator!")
# Get user input for password requirements
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

# Generate password components
password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)] 
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

# Combine all components
password_list = password_letters + password_symbols + password_numbers

# Shuffle the password list to ensure randomness
random.shuffle(password_list)

# Join the list into a string
password = ''.join(password_list)

# Output the generated password
print(f"Your password is: {password}")
