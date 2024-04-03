# Зчитування цілого числа з командного рядка
number = int(input("Введіть ціле число: "))

# Визначення парності або непарності числа
if number % 2 == 0:
    info = "Число {} є парним.".format(number)
else:
    info = "Число {} є непарним.".format(number)

# Запис інформації у текстовий файл
with open('number_info.txt', 'w') as file:
    file.write(info)

print("Інформацію про число збережено у файлі 'number_info.txt'.")
