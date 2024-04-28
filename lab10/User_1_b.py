# -*- coding: utf-8 -*-
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Доданий атрибут login_attempts зі значенням 0 за замовчуванням

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Користувач: {full_name}")
        print(f"Ім'я користувача: {self.username}")
        print(f"Електронна пошта: {self.email}")
        print(f"Місце розташування: {self.location}")

    def greeting_user(self):
        print(f"Привіт, {self.first_name}! Ласкаво просимо назад!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Створення екземпляру класу User
user = User("John", "Doe", "johndoe", "john.doe@example.com", "New York")

# Збільшення значення login_attempts та виведення його
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Кількість спроб входу: {user.login_attempts}")

# Скидання значення login_attempts і виведення його
user.reset_login_attempts()
print(f"Після скидання, кількість спроб входу: {user.login_attempts}")
