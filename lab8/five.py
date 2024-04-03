filename = 'guest_book.txt'

print("Ласкаво просимо! Введіть 'exit', щоб завершити.")

# Відкриття файлу у режимі додавання (якщо файл існує) або створення нового файлу
with open(filename, 'a') as file:
    while True:
        # Запит імені від користувача
        name = input("Будь ласка, введіть ваше ім'я: ")

        # Перевірка на вихід з циклу
        if name.lower() == 'exit':
            break

        # Виведення вітання та запис у файл
        greeting = "Ласкаво просимо, {}!\n".format(name)
        print(greeting)
        file.write(greeting)
