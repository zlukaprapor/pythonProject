# -*- coding: utf-8 -*-
# main2.py
from admin import Admin

# Створення екземпляру класу Admin
admin = Admin("Adam", "Smith", "adamsmith", "adam.smith@example.com", "New York")

# Виклик методу show_admin_privileges() для виведення привілеїв адміністратора
admin.show_admin_privileges()
