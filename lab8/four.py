# Відкриття файлу та зчитування кожного рядка
with open('learning_python.txt', 'r') as file:
    for line in file:
        # Заміна слова "Python" на "C" та виведення рядка на екран
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())
