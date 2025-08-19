# Import ASCII art logo from another file (art_day8.py)
from art import logo

# Print the logo when program starts
print(logo)

# List of alphabets to use for shifting letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Cipher function (works for both encoding and decoding)
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each character in the original text
    for letter in original_text:

        # Keep non-alphabet characters (like spaces, numbers, punctuation) unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the shifted position in alphabet
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # Wrap around if out of range
            output_text += alphabet[shifted_position]

    # Print the final result
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Flag to keep the program running until user chooses to exit
should_continue = True

while should_continue:
    # Ask user whether they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Get message and convert to lowercase for simplicity
    text = input("Type your message:\n").lower()

    # Get shift number (how many letters to move)
    shift = int(input("Type the shift number:\n"))

    # Call Caesar Cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
