# -*- coding: utf-8 -*-
import datetime

# Запис поточної дати і часу у файл today.txt
with open("today.txt", "w") as file:
    current_datetime = datetime.datetime.now()
    file.write(str(current_datetime))

# Зчитування даних з файлу today.txt
with open("today.txt", "r") as file:
    today_string = file.read()

# Розбір дати з рядка today_string
parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d %H:%M:%S.%f")
print("Поточна дата і час:", parsed_date)
