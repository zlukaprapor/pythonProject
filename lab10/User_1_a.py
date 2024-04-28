# -*- coding: utf-8 -*-
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Користувач: {full_name}")
        print(f"Ім'я користувача: {self.username}")
        print(f"Електронна пошта: {self.email}")
        print(f"Місце розташування: {self.location}")

    def greeting_user(self):
        print(f"Привіт, {self.first_name}! Ласкаво просимо назад!")


# Створення кількох екземплярів класу User
user1 = User("John", "Doe", "johndoe", "john.doe@example.com", "New York")
user2 = User("Alice", "Smith", "alicesmith", "alice.smith@example.com", "London")
user3 = User("Bob", "Johnson", "bobjohnson", "bob.johnson@example.com", "Los Angeles")

# Виклик методів для кожного користувача
user1.describe_user()
user1.greeting_user()
print()

user2.describe_user()
user2.greeting_user()
print()

user3.describe_user()
user3.greeting_user()
