# -*- coding: utf-8 -*-
# admin.py
from user import User

class Privileges:
    def __init__(self):
        self.privileges = ["Дозволено додавати повідомлення", "Дозволено видаляти користувачів", "Дозволено блокувати користувачів"]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()  # Створюємо екземпляр класу Privileges

    def show_admin_privileges(self):
        print("Ім'я адміністратора:", self.first_name)  # Вивід імені адміністратора
        self.privileges.show_privileges()  # Виклик методу show_privileges() через об'єкт privileges
