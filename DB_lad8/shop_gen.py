import mysql.connector
from faker import Faker
from tqdm import tqdm

fake = Faker()
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='026323',
    database='shop'
)
cursor = connection.cursor()

num_records = 1000000  # Кількість записів
batch_size = 10000  # Розмір партії для комітів

for i in tqdm(range(num_records // batch_size)):  # Цикл по партіях
    data = []
    for _ in range(batch_size):
        name = fake.word()
        category_id = fake.random_int(min=1, max=10)
        price = round(fake.random_number(digits=4) / 100, 2)
        data.append((name, category_id, price))

    cursor.executemany("INSERT INTO products (name, category_id, price) VALUES (%s, %s, %s)", data)
    connection.commit()

# Додавання залишкових записів, якщо їх кількість не кратна batch_size
remaining_records = num_records % batch_size
if remaining_records:
    data = []
    for _ in range(remaining_records):
        name = fake.word()
        category_id = fake.random_int(min=1, max=10)
        price = round(fake.random_number(digits=4) / 100, 2)
        data.append((name, category_id, price))

    cursor.executemany("INSERT INTO products (name, category_id, price) VALUES (%s, %s, %s)", data)
    connection.commit()

cursor.close()
connection.close()
