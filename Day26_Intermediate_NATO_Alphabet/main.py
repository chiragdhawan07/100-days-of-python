import pandas as pd

# Read the CSV file
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary: letter → code
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask user for a word
word = input("Enter a word: ").upper()

# Convert each letter into NATO code
result = [nato_dict[letter] for letter in word if letter in nato_dict]

print(result)
