import re

# Відкриття файлу для читання
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Пошук усіх слів, які починаються з літери "с"
words_starting_with_c = re.findall(r'\bc\w+', text, re.IGNORECASE)
print("Слова, які починаються з літери 'с':", words_starting_with_c)

# Пошук чотирилітерних слів, які починаються з літери "c"
four_letter_words_starting_with_c = re.findall(r'\bc\w{3}\b', text, re.IGNORECASE)
print("Чотирилітерні слова, які починаються з літери 'c':", four_letter_words_starting_with_c)

# Пошук слів, які закінчуються на букву "r"
words_ending_with_r = re.findall(r'\b\w+r\b', text, re.IGNORECASE)
print("Слова, які закінчуються на букву 'r':", words_ending_with_r)

# Пошук слів, які містять чотири літери "time" поспіль
words_containing_time = re.findall(r'\b\w*time\w*\b', text, re.IGNORECASE)
print("Слова, які містять 'time':", words_containing_time)
