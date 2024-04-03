# Відкриття файлу для читання та зчитування чисел
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Обчислення суми чисел
sum_of_numbers = sum(numbers)

# Виведення суми на екран
print("Сума чисел з файлу:", sum_of_numbers)

# Запис суми у інший файл
with open('sum_numbers.txt', 'w') as file:
    file.write(str(sum_of_numbers))
