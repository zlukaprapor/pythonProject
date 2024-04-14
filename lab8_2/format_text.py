# -*- coding: utf-8 -*-

def format_text(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            # Прочитати байти з файлу
            data = file.read()
            # Декодувати байти як текст у кодуванні cp1252
            text = data.decode('cp1252')
            # Заміна символів нового рядка на пропуски
            formatted_text = text.replace('\n', ' ')

        with open(output_file, 'w', encoding='utf-8') as file:
            # Запис відформатованого тексту у новий файл
            file.write(formatted_text)

        print(f"Успішно відформатовано текст і записано у файл {output_file}.")
    except FileNotFoundError:
        print("Файл не знайдено.")


# Задаємо назви вхідного та вихідного файлів
input_file = "book.txt"
output_file = "formatted_text.txt"

# Форматуємо вміст вхідного файлу та записуємо у вихідний файл
format_text(input_file, output_file)
