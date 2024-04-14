def calculate_letter_percentage(filename):
    try:
        with open(filename, 'r', encoding='cp1252') as file:
            text = file.read()

        total_letters = len([char for char in text if char.isalpha()])
        lowercase_letters = len([char for char in text if char.isalpha() and char.islower()])
        uppercase_letters = len([char for char in text if char.isalpha() and char.isupper()])

        lowercase_percentage = (lowercase_letters / total_letters) * 100 if total_letters > 0 else 0
        uppercase_percentage = (uppercase_letters / total_letters) * 100 if total_letters > 0 else 0

        print(f"У тексті {filename}:")
        print(f"Малих літер: {lowercase_percentage:.2f}%")
        print(f"Великих літер: {uppercase_percentage:.2f}%")
    except FileNotFoundError:
        print("Файл не знайдено.")

filename = "the_count_of_monte_cristo.txt"
calculate_letter_percentage(filename)
