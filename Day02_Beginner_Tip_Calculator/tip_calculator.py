# Day 2 - Tip Calculator
print("Welcome to the Tip Calculator!")

# Get inputs from user
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

# Calculate total with tip
bill_with_tip = total_bill * (1 + tip / 100)

# Calculate each person's share
each_person = bill_with_tip / people

# Display final amount (2 decimal places)
print(f"Each person should pay: ${each_person:.2f}")
