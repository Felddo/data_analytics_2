# Описание
Скрипт извлекает характеристики товаров (цена, бренд, категория) из текстовых описаний с помощью LLM (Groq API, модель llama-3.3-70b-versatile).

# Установка
pip install openai python-dotenv
Создать файл .env:
GROQ_API_KEY=your_api_key
# Запуск
python script.py

# Входные данные
Файл input.csv с колонкой description:
description
"Смартфон Samsung Galaxy S23 с экраном 6.1 дюйма, память 128 ГБ, стоимость 79999 рублей."

# Выходные данные
Файл output.json:
[
    {
        "description": "Смартфон Samsung Galaxy S23...",
        "price": "79999",
        "brand": "Samsung",
        "category": "Смартфон"
    }
]
