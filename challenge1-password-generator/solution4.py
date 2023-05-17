import random
import string

def generate_password():
    """Generate a random password."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    while True:
        try:
            pwd_length = int(input("Enter the desired password length (between 8 and 20): "))
            if pwd_length < 8 or pwd_length > 20:
                print("Invalid password length. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    pwd = ''
    for _ in range(pwd_length):
        pwd += random.choice(all_characters)

    while True:
        pwd = ''
        for _ in range(pwd_length):
            pwd += random.choice(all_characters)

        if (
            any(char in uppercase_letters for char in pwd)
            and any(char in lowercase_letters for char in pwd)
            and any(char in symbols for char in pwd)
            and sum(char in digits for char in pwd) >= 2
        ):
            break

    return pwd

result = generate_password()
print(result)
