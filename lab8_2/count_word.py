def count_word_occurrences(filename, word):
    try:
        with open(filename, 'rb') as file:
            # Прочитати байти з файлу
            data = file.read()
            # Декодувати байти як текст у кодуванні cp1252
            text = data.decode('cp1252')
            # Використовуємо lower() для ігнорування регістру
            word_lower = word.lower()
            # Рахуємо кількість входжень слова в тексті
            count = text.lower().count(word_lower)
            return count
    except FileNotFoundError:
        print("Файл не знайдено.")
        return -1

# Задаємо назви файлів та слово, кількість входжень якого ми хочемо знайти
files = ["file1.txt", "file2.txt", "file3.txt"]
search_word = "the"

# Проходимо по кожному файлу і виводимо кількість входжень слова
for file in files:
    count = count_word_occurrences(file, search_word)
    if count != -1:
        print(f"У файлі '{file}' слово '{search_word}' зустрічається {count} разів.")
