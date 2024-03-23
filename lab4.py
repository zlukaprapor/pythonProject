#1
# world_languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
# print("Початковий список мов світу:", world_languages)
# sorted_languages = sorted(world_languages)
# print("Список після сортування за алфавітом:", sorted_languages)
# reversed_languages = list(reversed(world_languages))
# print("Список після зворотного порядку:", reversed_languages)
# world_languages.sort(reverse=True)
# print("Список після сортування на місці у зворотному порядку:", world_languages)

#2
#input_numbers = input("Введіть числа, розділені пропусками: ")
# Розділення рядка на числа та конвертація їх в цілі числа
#numbers = [int(x) for x in input_numbers.split()]
#sum_of_numbers = sum(numbers)
#print("Сума чисел:", sum_of_numbers)

#3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
#Формування повідомлення з використанням 'and' перед останнім елементом
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(message)

#4
#input_string = input("Введіть рядок з 5 цифр, розділених пропусками: ")
# Розділення рядка на цифри та конвертація їх в цілі числа
#digits = [int(x) for x in input_string.split()]
#reversed_digits = sorted(digits, reverse=True)
# Формування числа з елементів нового списку
#result_number = int(''.join(map(str, reversed_digits)))
#print("Число, утворене об'єднанням елементів у зворотньому порядку:", result_number)

#5
#professions = ['Doctor', 'Engineer', 'Teacher', 'Artist', 'Programmer']
#sports = ['Football', 'Basketball', 'Swimming', 'Tennis', 'Cycling']
#family_members = ['John', 'Jane', 'Tom', 'Anna', 'David']
#oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

# Використання sorted()
#sorted_professions = sorted(professions)
#print("Список професій після сортування:", sorted_professions)

# Використання reverse()
#reversed_professions = list(reversed(professions))
#print("Список професій після зворотного порядку:", reversed_professions)

# Використання sort()
#sports.sort()
#print("Список видів спорту після сортування на місці:", sports)

# Використання join()
#family_string = ', '.join(family_members)
#print("Рядок із членами родини:", family_string)

# Використання count() для підрахунку кількості входжень
#count_atlantic = oceans.count('Atlantic')

# Виведення результату
#print(f"Кількість входжень 'Atlantic' у списку: {count_atlantic}")

#6

# keywords = ('for', 'if', 'else', 'in', ':')
#
# code_structure = [
#     ('for', 'each token in the postfix expression', ':'),
#         ('if', 'the token is a number', ':'),
#             ("print('Convert it to an integer and add it to the end of values')",),
#         ('else',),
#             ("print('Append the result to the end of values')",)
# ]
#
# def visualize_code(structure, indentation=4):
#     for line in structure:
#         print(' ' * indentation * line.count(' '), end='')
#         print(' '.join(line))
#
# visualize_code(code_structure)
