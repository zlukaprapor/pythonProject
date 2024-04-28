# -*- coding: utf-8 -*-
from User_1_a import User
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ["Дозволено додавати повідомлення", "Дозволено видаляти користувачів", "Дозволено блокувати користувачів"]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges:
            print(privilege)


# Створення екземпляру класу Admin
admin = Admin("Adam", "Smith", "adamsmith", "adam.smith@example.com", "New York")

# Виклик методу show_privileges() для виведення привілеїв адміністратора
admin.show_privileges()
