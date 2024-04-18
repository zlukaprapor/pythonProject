# -*- coding: utf-8 -*-
import os

source_file_path = "chapters.txt"  # замініть шлях на перший файл
destination_file_path = "chapters2.txt"  # замініть шлях на другий файл

# Копіювання даних з одного файлу у інший
with open(source_file_path, 'r') as source_file:
    data = source_file.read()
    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(data)

# Зчитування скопійованих даних і виведення їх на екран
with open(destination_file_path, 'r') as destination_file:
    copied_data = destination_file.read()
    print("Скопійовані дані:", copied_data)

# Видалення першого файла
os.remove(source_file_path)
