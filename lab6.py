#1
# Створення списку користувачів
#
# users = ['Admin', 'Alex', 'John', 'Jane']
#
# # Перевірка, чи список користувачів не порожній
# if users:
#     for user in users:
#         # Виведення особливого повідомлення для користувача 'Admin'
#         if user == 'Admin':
#             print(f"Hello {user}, I hope you’re well.")
#         else:
#             print(f"Hello {user}, thank you for logging in again.")
# else:
#     print("We need to find some users!")
#
# # Видалення всіх імен користувачів
# users.clear()
#
# # Перевірка, чи список користувачів не порожній після видалення
# if users:
#     for user in users:
#         # Виведення особливого повідомлення для користувача 'Admin'
#         if user == 'Admin':
#             print(f"Hello {user}, I hope you’re well.")
#         else:
#             print(f"Hello {user}, thank you for logging in again.")
# else:
#     print("We need to find some users!")


#2
# Запит від користувача щодо кількості сторін
# num_sides = int(input("Введіть кількість сторін (від 3 до 6): "))
#
# # Визначення назви геометричної фігури
# if 3 <= num_sides <= 6:
#     if num_sides == 3:
#         shape_name = "Трикутник"
#     elif num_sides == 4:
#         shape_name = "Чотирикутник (Квадрат, Прямокутник і т.д.)"
#     elif num_sides == 5:
#         shape_name = "П'ятикутник"
#     else:
#         shape_name = "Шестикутник"
#
#     print(f"Фігура з {num_sides} сторін - це {shape_name}.")
# else:
#     print("Невірна кількість сторін. Введіть число від 3 до 6.")

#3
# Створення списку чисел від 1 до 9
# numbers = list(range(1, 10))
#
# # Цикл для виведення правильного закінчення числівника
# for num in numbers:
#     if num == 1:
#         suffix = "st"
#     elif num == 2:
#         suffix = "nd"
#     elif num == 3:
#         suffix = "rd"
#     else:
#         suffix = "th"
#
#     print(f"{num}{suffix}")


#4
# # Запит від користувача для введення цілого числа
# user_input = input("Введіть ціле число: ")
#
# # Перевірка, чи введено ціле число
# if user_input.isdigit():
#     number = int(user_input)
#
#     # Визначення парності числа
#     if number % 2 == 0:
#         print(f"Число {number} є парним.")
#     else:
#         print(f"Число {number} є непарним.")
# else:
#     print("Введене значення не є цілим числом.")

#5
# Запит від користувача для введення назви місяця
# month_name = input("Введіть назву місяця: ")
#
# # Перевірка кількості днів у місяці
# if month_name.lower() in ["січень", "березень", "травень", "липень", "серпень", "жовтень", "грудень"]:
#     days = 31
# elif month_name.lower() in ["квітень", "червень", "вересень", "листопад"]:
#     days = 30
# elif month_name.lower() == "лютий":
#     # Зчитування року від користувача для визначення, чи це високосний рік
#     year = int(input("Введіть рік: "))
#
#     # Визначення кількості днів у лютому
#     #year % 4 == 0: Рік повинен бути кратним 4, щоб бути високосним.
#     #year % 100 != 0: Рік не повинен бути кратним 100, якщо він не є високосним.
#     #year % 400 == 0: Але якщо рік кратний 400, він все одно є високосним.
#
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         days = 29  # високосний рік
#     else:
#         days = 28  # не високосний рік
# else:
#     print("Введена некоректна назва місяця.")
#     days = None
#
# # Виведення кількості днів у місяці
# if days is not None:
#     print(f"У місяці {month_name} {days} днів.")

#6
# Зчитування року від користувача
# year = int(input("Введіть рік: "))
#
# # Перевірка, чи є рік високосним
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("рік високосний.")
# else:
#     print("рік невисокосний.")

#7
# # Ініціалізація змінної для зберігання суми
# total_sum = 0
#
# # Зчитування чисел зі стандартного вводу
# while True:
#     # Зчитування цілого числа з рядка
#     num = int(input("Введіть ціле число (введіть 0 для завершення): "))
#
#     # Перевірка умови завершення введення
#     if num == 0:
#         break
#
#     # Додавання числа до суми
#     total_sum += num
#
# # Виведення суми
# print(f"Сума введених чисел: {total_sum}")

#8
# # Зчитування цілих чисел зі стандартного вводу
# while True:
#     try:
#         # Зчитування цілого числа з рядка
#         num = int(input("Введіть ціле число: "))
#
#         # Перевірка умов
#         if num < 10:
#             # Пропускаємо числа менше 10
#             continue
#         elif num > 100:
#             # Припиняємо зчитування чисел, якщо число більше 100
#             break
#         else:
#             # Виведення числа, якщо воно відповідає умовам
#             print(num)
#     except ValueError:
#         # Обробка помилки, якщо введено не ціле число
#         print("Будь ласка, введіть ціле число.")

#9
# def calculator():
#     try:
#         # Зчитування першого числа
#         num1 = float(input("Введіть перше число: "))
#
#         # Зчитування операції
#         operation = input("Введіть операцію (+, -, *, /, mod, pow, div): ")
#
#         # Зчитування другого числа
#         num2 = float(input("Введіть друге число: "))
#
#         # Виконання операції та виведення результату
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             # Обробка ділення на 0
#             if num2 == 0:
#                 raise ZeroDivisionError("Division by zero!")
#             result = num1 / num2
#         elif operation == 'mod':
#             # Обробка взяття залишку
#             result = num1 % num2
#         elif operation == 'pow':
#             # Обробка піднесення до степеня
#             result = num1 ** num2
#         elif operation == 'div':
#             # Обробка цілочисельного ділення
#             result = num1 // num2
#         else:
#             print("Невідома операція. Будь ласка, введіть коректну операцію.")
#             return
#
#         print(f"Результат: {result}")
#
#     except ValueError:
#         print("Будь ласка, введіть коректні числа.")
#     except ZeroDivisionError as e:
#         print(e)
#
# # Виклик функції калькулятора
# calculator()

#10
# def ukrainian_banknotes():
#     # Словник з номіналами та іменами осіб на банкнотах
#     banknotes = {
#         20: "Іван Франко",
#         50: "Михайло Грушевський",
#         100: "Тарас Шевченко",
#         200: "Леся Українка",
#         500: "Григорій Сковорода",
#         1000: "Володимир Вернадський"
#     }
#
#     try:
#         # Зчитування номіналу банкноти від користувача
#         nominal = int(input("Введіть номінал банкноти: "))
#
#         # Перевірка чи існує введений номінал у словнику
#         if nominal in banknotes:
#             print(f"Номінал: {nominal}, Особа: {banknotes[nominal]}")
#         else:
#             print("Банкнота з таким номіналом не існує.")
#     except ValueError:
#         print("Будь ласка, введіть ціле число.")
#
# # Виклик функції для виведення імен на банкнотах
# ukrainian_banknotes()


