#1
# glossary = {
#     'Variable': 'A named storage location in a program that stores data and can be manipulated during runtime.',
#     'Function': 'A reusable block of code that performs a specific task. It can take input, process it, and return a result.',
#     'List': 'An ordered collection of items. Lists are mutable, meaning their elements can be changed or modified.',
#     'Dictionary': 'A collection of key-value pairs, where each key must be unique. Dictionaries are unordered.',
#     'Loop': 'A control flow statement that allows code to be executed repeatedly based on a certain condition.',
# }
#
# for term, definition in glossary.items():
#     print(f"{term}:\n\t{definition}\n")

#2
# rivers_regions = {
#     'Amazon': 'South America',
#     'Nile': 'Africa',
#     'Yangtze': 'Asia',
# }
#
# for river, region in rivers_regions.items():
#     print(f"The {river} runs through {region}.")

#3
# programming_languages = {
#     'Python': 'Guido van Rossum',
#     'JavaScript': 'Brendan Eich',
#     'Java': 'James Gosling',
#     'C++': 'Bjarne Stroustrup',
# }
#
# # Виведення повідомлень
# for language, developer in programming_languages.items():
#     print(f"My favorite programming language is {language}. It was created by {developer}.")
#
# # Видалення однієї пари "мова: розробник"
# del programming_languages['C++']
#
# # Виведення словника після видалення
# print("\nDictionary after deletion:")
# print(programming_languages)

#4
# Створення англо-німецького словника
# e2g = {
#     'stork': 'storch',
#     'hawk': 'falke',
#     'woodpecker': 'specht',
#     'owl': 'eule',
# }
#
# # Виведення словника на екран
# print("English to German Dictionary:")
# print(e2g)
#
# # Виведення німецького варіанту слова "owl"
# german_translation_of_owl = e2g['owl']
# print("\nThe German translation of 'owl' is:", german_translation_of_owl)
#
# # Додавання ще двох слів у словник
# e2g['dog'] = 'hund'
# e2g['cat'] = 'katze'
#
# # Виведення словника після додавання
# print("\nDictionary after adding two more words:")
# print(e2g)
#
# # Виведення ключів та значень словника у вигляді списків
# keys_list = list(e2g.keys())
# values_list = list(e2g.values())
#
# print("\nKeys of the dictionary:")
# print(keys_list)
#
# print("\nValues of the dictionary:")
# print(values_list)

#5
# # Створення словників для домашніх тварин
# pet1 = {'name': 'Bella', 'species': 'dog', 'owner': 'John'}
# pet2 = {'name': 'Mittens', 'species': 'cat', 'owner': 'Alice'}
# pet3 = {'name': 'Rocky', 'species': 'hamster', 'owner': 'Bob'}
#
# # Збереження словників у списку
# pets = [pet1, pet2, pet3]
#
# # Виведення повідомлень про власників та їхніх улюбленців
# for pet in pets:
#     print(f"{pet['owner']} is the owner of a pet - a {pet['species']}, named {pet['name']}.")

#6
# morse_code = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..'
# }
#
# def text_to_morse(text):
#     morse_representation = ''
#     for char in text:
#         if char.upper() in morse_code:
#             morse_representation += morse_code[char.upper()] + ' '
#         else:
#             morse_representation += char + ' '
#     return morse_representation.strip()
#
# Запит користувача
# user_input = input("Введіть букву: ")
#
# Виведення представлення букви у символах азбуки Морзе
# result = text_to_morse(user_input)
# print(f"Представлення букви '{user_input}' у символах азбуки Морзе: {result}")

#7
# subjects = {
#     'science': {
#         'physics': ['nuclear physics', 'optics', 'thermodynamics'],
#         'computer science': {},
#         'biology': {}
#     },
#     'humanities': {},
#     'public': {}
# }
#
# # Виведення ключів subjects['science'] і значень subjects['science']['physics']
# print("Ключі subjects['science']:", subjects['science'].keys())
# print("Значення subjects['science']['physics']:", subjects['science']['physics'])

#8
# cities = {
#     'Kyiv': {
#         'country': 'Ukraine',
#         'population': 2800000,
#         'fact': 'Kyiv is the capital and largest city of Ukraine.'
#     },
#     'Paris': {
#         'country': 'France',
#         'population': 2148000,
#         'fact': 'Paris is known as the "City of Love" and the "City of Lights".'
#     },
#     'Tokyo': {
#         'country': 'Japan',
#         'population': 13960000,
#         'fact': 'Tokyo is the most populous city in Japan and one of the most populous metropolitan areas in the world.'
#     }
# }
#
# # Виведення інформації про кожне місто
# for city, info in cities.items():
#     print(f"{city}:")
#     print(f"\tCountry: {info['country']}")
#     print(f"\tPopulation: {info['population']}")
#     print(f"\tFact: {info['fact']}\n")

#9
# import random
#
# # Створення словника teams
# teams = {
#     'Los Angeles Lakers': [20, 15, 1, 4, 150],
#     'Golden State Warriors': [21, 18, 0, 3, 175],
#     'Houston Rockets': [19, 12, 2, 5, 140],
#     'Boston Celtics': [22, 17, 1, 4, 160],
#     'Miami Heat': [20, 14, 1, 5, 155]
# }
#
# # Виведення статистики кількох команд NBA
# for team, stats in teams.items():
#     print(f"{team.upper()} {stats[0]} {stats[1]} {stats[2]} {stats[3]} {stats[4]}")

#10
# Створення словника things
things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}

# Виведення повідомлення про усі речі гравця
print("Equipment:")
total_things = 0
for item, quantity in things.items():
    print(f"{quantity} {item}")
    total_things += quantity

print(f"Total number of things: {total_things}")

