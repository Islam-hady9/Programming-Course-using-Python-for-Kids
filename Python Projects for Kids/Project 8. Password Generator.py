import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

password_generator()