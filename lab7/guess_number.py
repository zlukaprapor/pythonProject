

def guess_number(secret_number, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Вгадайте число: "))
            if guess == secret_number:
                print("Вітаємо! Ви вгадали число!")
                return
            elif guess < secret_number:
                print("Загадане число більше.")
            else:
                print("Загадане число менше.")
            attempts += 1
        except ValueError:
            print("Введіть ціле число.")
    print(f"Ви програли. Загадане число було: {secret_number}")