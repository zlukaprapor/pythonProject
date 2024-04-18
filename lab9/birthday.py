# -*- coding: utf-8 -*-

import datetime

# Дата народження
happy = datetime.datetime(1987, 5, 11)

# Функція для виведення відповідей у файл
def save_answer(question, answer):
    with open("answers.txt", "a") as file:
        file.write(question + ": " + answer + "\n")

# "Яка дата вашого народження?"
question1 = "Яка дата вашого народження?"
answer1 = happy.strftime("%Y-%m-%d")
print(question1, answer1)
save_answer(question1, answer1)

# "У який день тижня ви народилися?"
question2 = "У який день тижня ви народилися?"
answer2 = happy.strftime("%A")
print(question2, answer2)
save_answer(question2, answer2)

# "Коли вам буде (або вже було) 13 330 днів від народження?"
question3 = "Коли вам буде (або вже було) 13 330 днів від народження?"
future_date = happy + datetime.timedelta(days=13330)
answer3 = future_date.strftime("%Y-%m-%d")
print(question3, answer3)
save_answer(question3, answer3)
