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

    # select randomly chaaracters from all_characters and specifying the length
    choices = random.choices(all_characters, k=length)
    
    #joinig the characters to remove white spaces
    password = ''.join(choices)
    
    # returning the function
    return password

# calling the generate_password function
password = generate_password()

# printig the result to console
print(password)
