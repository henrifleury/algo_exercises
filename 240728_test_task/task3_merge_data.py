'''3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников. Первый источник - это CSV-файл с информацией о
продуктах (поля: product_id, product_name). Второй источник - это JSON-файл с данными о продажах (поля: sale_id,
product_id, amount). Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах
для каждого продукта.

Ваш код здесь
'''

import pandas as pd

products_df = pd.read_csv('products.csv')

sales_df = pd.read_json('sales.json')

merged_df = pd.merge(products_df, sales_df, on='product_id', how='left')

print(merged_df[['product_id', 'product_name', 'sale_id', 'amount']])