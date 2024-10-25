'''
Добрый день, просим пройти Тестовое задание для кандидата на позицию программиста Python

1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API и получает данные. Например, используйте публичное API https://jsonplaceholder.typicode.com/posts. Сохраните полученные данные в формате JSON в файл.

Ваш код здесь

2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

Ваш код здесь

3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников. Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name). Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount). Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.

Ваш код здесь

4. Оптимизация скрипта
Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.

Исходный скрипт

numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
squares.append(number ** 2)
Оптимизированный скрипт
Ваш код здесь


Ответы на задания просьба отправить на zackizyanovaa@yandex.ru с темой "Тестовое задание для программиста Python - [Ваше имя]". Дедлайн 01.08.2024 19:00 по МСК.

Удачи! Мы ждем ваши ответы.
'''

import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)

import requests
import json

# URL API
url = "https://jsonplaceholder.typicode.com/posts"

# Выполнение GET-запроса к API
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Получение данных в формате JSON
    data = response.json()

    # Сохранение данных в файл
    with open('posts.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Данные успешно сохранены в файл 'posts.json'.")
else:
    print(f"Ошибка при получении данных: {response.status_code}")

