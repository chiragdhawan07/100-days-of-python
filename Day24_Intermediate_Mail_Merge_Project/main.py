# Read invited names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the letter template
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Create personalized letters
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
