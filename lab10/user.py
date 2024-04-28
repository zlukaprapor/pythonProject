# -*- coding: utf-8 -*-
# user.py

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("Користувач:", self.first_name, self.last_name)
        print("Ім'я користувача:", self.username)
        print("Електронна пошта:", self.email)
        print("Місце розташування:", self.location)

    def greeting_user(self):
        print("Привіт,", self.first_name + "!", "Ласкаво просимо назад!")
