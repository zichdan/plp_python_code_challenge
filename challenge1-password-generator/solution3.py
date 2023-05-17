import random
import string

def generate_password(length=8):
    """Generate a random password."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # sum of all characters listed
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # Ensure password length meets minimum requirement
    if length < 8:
        length = 8

    # select randomly characters from all_characters and specifying the length
    choices = random.choices(all_characters, k=length)

    # joining the characters to remove white spaces
    password = ''.join(choices)

    # returning the password
    return password

# Prompt the user for the desired password length
length_input = input("Enter the desired password length (default is 8): ")

# Convert the input to an integer or use the default value if no input is provided
password_length = int(length_input) if length_input else 8

# Generate the password with the specified length
password = generate_password(password_length)

# Print the result to the console
print("Generated password:", password)
