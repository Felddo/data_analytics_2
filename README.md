# Описание
Скрипт извлекает характеристики товаров (цена, бренд, категория) из текстовых описаний с помощью LLM (Groq API, модель llama-3.3-70b-versatile).

### Установка
1. git clone https://github.com/Felddo/data_analytics_2
2. cd data_analytics_2
3. pip install -r requirements.txt
4. Делаем ключ на сайте https://console.groq.com/keys
5. Вставляем в файл .env свой ключ "GROQ_API_KEY==ключ"
6. python main.py

### Входные данные
Первые 2 строчки файла input.csv с колонкой description:
```csv
description
"Смартфон Samsung Galaxy S23 с экраном 6.1 дюйма, память 128 ГБ, стоимость 79999 рублей."
"Ноутбук Lenovo IdeaPad 3 с процессором Intel Core i5, 16 ГБ ОЗУ, цена 65990 руб."
```

### Выходные данные
Первые 2 строчки файла output.json:
```json
[
    {
        "description": "Смартфон Samsung Galaxy S23 с экраном 6.1 дюйма, память 128 ГБ, стоимость 79999 рублей.",
        "price": "79999",
        "brand": "Samsung",
        "category": "Смартфон"
    },
    {
        "description": "Ноутбук Lenovo IdeaPad 3 с процессором Intel Core i5, 16 ГБ ОЗУ, цена 65990 руб.",
        "price": "65990",
        "brand": "Lenovo",
        "category": "Ноутбук"
    }
]
```
