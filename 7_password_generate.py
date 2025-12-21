import random
import string

def generate_password(length):
    # All possible characters
    letters = string.ascii_letters   # a-zA-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # !@#$%^&*()_+
    
    # Combine all characters
    all_chars = letters + digits + symbols
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter the length of your password: "))
password = generate_password(length)
print("Your generated password is:", password)
