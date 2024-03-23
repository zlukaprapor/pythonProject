#11
# def get_square_color(position):
#     column, row = position[0], int(position[1])
#     # Перевірка на парність рядка і стовпчика
#     if (ord(column) - ord('a') + row) % 2 == 0:
#         return "black"
#     else:
#         return "white"
#
# def main():
#     position = input("Введіть позицію шахової фігури (наприклад, a1, d5): ")
#     color = get_square_color(position)
#     print(f"Квадрат має колір {color}")
#
# if __name__ == "__main__":
#     main()


#12  Level noon
# def is_palindrome(s):
#     # Перетворюємо рядок у нижній регістр та видаляємо пробіли
#     s = s.lower().replace(" ", "")
#     # Перевіряємо, чи рядок співпадає зі своїм відображенням
#     return s == s[::-1]
#
# def main():
#     while True:
#         user_input = input("Введіть рядок (або 'escape' для виходу): ")
#         if user_input.lower() == "escape":
#             print("Програма завершила роботу.")
#             break
#         if is_palindrome(user_input):
#             print("Це паліндром.")
#         else:
#             print("Це не паліндром.")
#
# if __name__ == "__main__":
#     main()

#13
# def multiplication_table(rows, cols):
#     for i in range(1, rows + 1):
#         for j in range(1, cols + 1):
#             print(f"{i} * {j} = {i * j}", end="\t")
#         print()
#
# def main():
#     try:
#         rows = int(input("Введіть кількість рядків: "))
#         cols = int(input("Введіть кількість стовпців: "))
#         if rows <= 0 or cols <= 0:
#             print("Розмірність таблиці повинна бути додатнім числом.")
#             return
#         multiplication_table(rows, cols)
#     except ValueError:
#         print("Введіть ціле число для кількості рядків і стовпців.")
#
# if __name__ == "__main__":
#     main()

#14
# Як відомо, День програміста припадає на 256 день року,
# у невисокосний рік це 13 вересня, а у високосний - 12.
# Дізнайтеся число і номер місяця, що припадають на день,
# за номером n, який вводиться користувачем, у невисокосному
# 2017 році.

#15
# def decimal_to_binary(decimal):
#     if decimal == 0:
#         return "0"
#
#     result = ""
#     q = decimal
#
#     while q != 0:
#         r = q % 2
#         result = str(r) + result
#         q //= 2
#
#     return result
#
#
# def main():
#     try:
#         decimal = int(input("Введіть десяткове число: "))
#         if decimal < 0:
#             print("Десяткове число повинно бути додатнім.")
#             return
#         binary = decimal_to_binary(decimal)
#         print(f"{decimal} у десятковій системі - {binary} у двійковій системі.")
#     except ValueError:
#         print("Введіть ціле число.")
#
#
# if __name__ == "__main__":
#     main()

#16
# def caesar_cipher(message, shift):
#     encrypted_message = ""
#     for char in message:
#         if char.isalpha():
#             # Визначаємо зсув для великих і малих літер
#             if char.islower():
#                 base = ord('a')
#             else:
#                 base = ord('A')
#             # Зсув у межах алфавіту
#             shifted_char = chr((ord(char) - base + shift) % 26 + base)
#         else:
#             # Якщо символ не є літерою, додаємо його незмінним
#             shifted_char = char
#         encrypted_message += shifted_char
#     return encrypted_message
#
# def main():
#     message = input("Введіть повідомлення: ")
#     shift = int(input("Введіть зсув: "))
#     encrypted_message = caesar_cipher(message, shift)
#     print("Зашифроване повідомлення:", encrypted_message)
#
# if __name__ == "__main__":
#     main()

#17
# import random
#
# def generate_random_password():
#     password_length = random.randint(7, 10)
#     password = ""
#     for _ in range(password_length):
#         password += chr(random.randint(33, 126))
#     return password
#
# def main():
#     random_password = generate_random_password()
#     print("Випадковий пароль:", random_password)
#
# if __name__ == "__main__":
#     main()

#18
# import random
#
# def guess_number(secret_number, max_attempts):
#     attempts = 0
#     while attempts < max_attempts:
#         try:
#             guess = int(input("Вгадайте число: "))
#             if guess == secret_number:
#                 print("Вітаємо! Ви вгадали число!")
#                 return
#             elif guess < secret_number:
#                 print("Загадане число більше.")
#             else:
#                 print("Загадане число менше.")
#             attempts += 1
#         except ValueError:
#             print("Введіть ціле число.")
#     print(f"Ви програли. Загадане число було: {secret_number}")
#
# def main():
#     max_number = 100
#     secret_number = random.randint(1, max_number)
#     max_attempts = 5
#     print("Комп'ютер загадав число від 1 до 100. Спробуйте вгадати за 5 спробами.")
#     guess_number(secret_number, max_attempts)
#
# if __name__ == "__main__":
#     main()

#19
# import random
#
# def get_computer_choice():
#     return random.choice(["Камінь", "Ножиці", "Папір"])
#
# def get_user_choice():
#     while True:
#         choice = input("Виберіть Камінь, Ножиці або Папір: ").capitalize()
#         if choice in ["Камінь", "Ножиці", "Папір"]:
#             return choice
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")
#
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "Нічия!"
#     elif (user_choice == "Камінь" and computer_choice == "Ножиці") or \
#          (user_choice == "Ножиці" and computer_choice == "Папір") or \
#          (user_choice == "Папір" and computer_choice == "Камінь"):
#         return "Ви виграли!"
#     else:
#         return "Комп'ютер виграв."
#
# def play_game():
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()
#     print(f"Ваш вибір: {user_choice}")
#     print(f"Вибір комп'ютера: {computer_choice}")
#     print(determine_winner(user_choice, computer_choice))
#
# def main():
#     while True:
#         play_game()
#         play_again = input("Хочете зіграти ще раз? (так/ні): ").lower()
#         if play_again != "так":
#             break
#
# if __name__ == "__main__":
#     main()
