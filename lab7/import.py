import random

from square_color import get_square_color
from palindrome import is_palindrome
from multiplication_table import multiplication_table
from decimal_to_binary import decimal_to_binary
from caesar_cipher import caesar_cipher
from generate_random_password import generate_random_password
from guess_number import guess_number
from rock_paper_scissors import main

# Виклик функції get_square_color
position = input("Введіть позицію шахової фігури (наприклад, a1, d5): ")
color = get_square_color(position)
print(f"Квадрат має колір {color}")

# Виклик функції is_palindrome
while True:
    user_input = input("Введіть рядок (або '1' для виходу): ")
    if user_input.lower() == "1":
        print("Програма завершила роботу.")
        break
    if is_palindrome(user_input):
        print("Це паліндром.")
    else:
        print("Це не паліндром.")

# Виклик функції multiplication_table
try:
    rows = int(input("Введіть кількість рядків: "))
    cols = int(input("Введіть кількість стовпців: "))
    if rows <= 0 or cols <= 0:
        print("Розмірність таблиці повинна бути додатнім числом.")
    else:
        multiplication_table(rows, cols)
except ValueError:
    print("Введіть ціле число для кількості рядків і стовпців.")


# Виклик функції decimal_to_binary
try:
    decimal = int(input("Введіть десяткове число: "))
    if decimal < 0:
        print("Десяткове число повинно бути додатнім.")
    else:
        binary = decimal_to_binary(decimal)
        print(f"{decimal} у десятковій системі - {binary} у двійковій системі.")
except ValueError:
    print("Введіть ціле число.")

# Виклик функції caesar_cipher
message = input("Введіть повідомлення: ")
shift = int(input("Введіть зсув: "))
encrypted_message = caesar_cipher(message, shift)
print("Зашифроване повідомлення:", encrypted_message)

# Виклик функції generate_random_password
random_password = generate_random_password()
print("Випадковий пароль:", random_password)

# Виклик функції guess_number
max_number = 100
secret_number = random.randint(1, max_number)
max_attempts = 5
print("Комп'ютер загадав число від 1 до 100. Спробуйте вгадати за 5 спробами.")
guess_number(secret_number, max_attempts)

# Виклик функції play_game
main()
