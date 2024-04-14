import sqlite3

# Функція для створення таблиці ratings
def create_ratings_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings (
                        id INTEGER PRIMARY KEY,
                        title VARCHAR(100),
                        year INT,
                        rating FLOAT
                    )''')

# Функція для додавання даних зі списку imdb до таблиці ratings
def fill_ratings_table(cursor, conn, imdb):
    for movie in imdb:
        cursor.execute('INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)',
                       (movie['title'], movie['year'], movie['rating']))
    conn.commit()

# Функція для виведення всіх записів таблиці ratings у алфавітному порядку за полем title
def print_all_ratings(cursor):
    cursor.execute('SELECT * FROM ratings ORDER BY title ASC')
    rows = cursor.fetchall()
    print("Усі записи таблиці ratings у алфавітному порядку за полем title:")
    for row in rows:
        print(row)

# Функція для виведення записів таблиці ratings з рейтингом більшим за 8.70
def print_high_ratings(cursor):
    cursor.execute('SELECT * FROM ratings WHERE rating > 8.70')
    rows = cursor.fetchall()
    print("Записи таблиці ratings з рейтингом більшим за 8.70:")
    for row in rows:
        print(row)

# Функція для зчитування даних з файлу
def read_data_from_file(filename):
    imdb = []
    with open(filename, 'r', encoding='utf-8') as file:
        next(file)  # Пропустити перший рядок з заголовками
        for line in file:
            data = line.strip().split(',')  # Розділити рядок по комі
            movie = {
                'title': data[0],
                'year': int(data[1]),
                'rating': float(data[2])
            }
            imdb.append(movie)
    return imdb

# Підключення до бази даних
conn = sqlite3.connect('imdb.db')
cursor = conn.cursor()

# Створення таблиці ratings
create_ratings_table(cursor)

# Зчитування даних з файлу
filename = 'imdb.csv'
imdb = read_data_from_file(filename)

# Додавання даних зі списку imdb до таблиці ratings
fill_ratings_table(cursor, conn, imdb)

# Виведення всіх записів таблиці ratings у алфавітному порядку за полем title
print_all_ratings(cursor)

# Виведення записів таблиці ratings з рейтингом більшим за 8.70
print_high_ratings(cursor)

# Закриття з'єднання з базою даних
conn.close()
