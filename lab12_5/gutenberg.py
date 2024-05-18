import requests

# Виконуємо GET-запит до сайту gutenberg.org
response = requests.get("https://www.gutenberg.org")

# Виводимо на екран інформацію про статус запиту
print("Статус запиту:", response.status_code)

# Виводимо на екран інформацію про кодування сторінки
print("Кодування сторінки:", response.encoding)
