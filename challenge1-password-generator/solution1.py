import random
import string

def generate_password():
    """Generate a random password."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # sum of all characters listed
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # selecting randomly from numbers between min of 8 and max 0f 20
    password_length = random.randint(8, 20)
    
    # definig password variable
    password = ''

    # select randomly and joining from all_characters using a "while loop"
    while True:
        password = ''.join(random.choice(all_characters) for _ in range(password_length))
       
        # making sure all required criteria are satisfied   
        if (any(char in uppercase_letters for char in password)
            and any(char in lowercase_letters for char in password)
            and any(char in symbols for char in password)
            and sum(char in digits for char in password) >= 2):
            break
    return password

result = generate_password()
print(result)
