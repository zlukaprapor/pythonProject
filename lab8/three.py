# Зчитування файлу та виведення його вмісту з використанням блоку with
with open('learning_python.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Відкриття файлу та зчитування його вмісту у список
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

# Виведення вмісту файлу, який збережено у списку
print("\nЗміст файлу, зчитаний у список:")
for line in lines:
    print(line.strip())
