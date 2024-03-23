import random

def generate_random_password():
    password_length = random.randint(7, 10)
    password = ""
    for _ in range(password_length):
        password += chr(random.randint(33, 126))
    return password