import csv
import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

results = []

with open("input.csv", "r", encoding="utf-8-sig") as f_in:
    reader = csv.DictReader(f_in)

    for row in reader:
        description = row["description"]
        prompt = (
            "Извлеки характеристики товара из описания. "
            "Верни только JSON в формате:\n"
            '{"price": "...", "brand": "...", "category": "..."}\n\n'
            f"Описание товара:\n{description}"
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content.strip()
        content = content.replace("```json", "").replace("```", "").strip()

        data = json.loads(content)
        results.append({"description": description, **data})

        time.sleep(2)

with open("output.json", "w", encoding="utf-8-sig") as f_out:
    json.dump(results, f_out, ensure_ascii=False, indent=4)
