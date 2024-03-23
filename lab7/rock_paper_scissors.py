import random

def get_computer_choice():
    return random.choice(["Камінь", "Ножиці", "Папір"])

def get_user_choice():
    while True:
        choice = input("Виберіть Камінь, Ножиці або Папір: ").capitalize()
        if choice in ["Камінь", "Ножиці", "Папір"]:
            return choice
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "Камінь" and computer_choice == "Ножиці") or \
         (user_choice == "Ножиці" and computer_choice == "Папір") or \
         (user_choice == "Папір" and computer_choice == "Камінь"):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

def main():
    while True:
        play_game()
        play_again = input("Хочете зіграти ще раз? (так/ні): ").lower()
        if play_again != "так":
            break