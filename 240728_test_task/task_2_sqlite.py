'''2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

Ваш код здесь
'''

import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

# поле возраст не очень удобно
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Марья', 28)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Иван', 35)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Бармалей', 40)")
connection.commit()

cursor.execute("SELECT name, age FROM users WHERE age > 30")

# Получение всех результатов запроса
results = cursor.fetchall()

# Вывод имен и возраста пользователей
for row in results:
    name, age = row
    print(f"Имя: {name}, Возраст: {age}")

# Закрытие курсора и соединения с базой данных
cursor.close()
connection.close()