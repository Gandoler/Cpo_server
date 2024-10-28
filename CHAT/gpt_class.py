import requests
from JSON_DATA import JSON_DATA_LOADER
import random

class gpt_class:
    def __init__(self):
        self.data = JSON_DATA_LOADER.load_config()
        if self.data:
            self.api_key = self.data.get("CHATIK")  # Ваш ключ API
    @staticmethod
    def birthday_greeting(name):
        greetings = [
            f"С днём рождения, {name}! Пусть каждый день будет наполнен счастьем и улыбками!",
            f"Поздравляю с днём рождения, {name}! Пусть все мечты сбываются, а впереди ждёт только радость!",
            f"Дорогой {name}, с днём рождения! Желаю много счастья, здоровья и успехов!",
            f"{name}, поздравляю с твоим праздником! Пусть каждый момент будет незабываемым, а каждый день – лучшим!",
            f"Счастья, любви и удачи тебе, {name}! С днём рождения! Пусть в твоей жизни будет много ярких событий!",
            f"{name}, желаю тебе невероятного дня рождения! Пусть жизнь радует тебя сюрпризами и возможностями!",
            f"С днём рождения, {name}! Пусть всегда рядом будут верные друзья, а удача сопровождает во всем!",
        ]
        return random.choice(greetings)

    def generate_congratulation(self, name, interests):
        prompt = f"Write congratulations for {name}, that interested {interests}. congratulations must be friendly."

        url = "https://api-inference.huggingface.co/models/gpt2-large"  # Замените на правильный URL для модели
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 400,
                "temperature":0.9,
            },
        }

        try:
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                generated_text = response.json()[0]['generated_text']
                return generated_text.strip()
            else:
                print(f"Ошибка: {response.status_code}, {response.text}")
                return "Не удалось сгенерировать поздравление."
        except Exception as e:
            print(f"Ошибка при обращении к API: {e}")
            return "Не удалось сгенерировать поздравление."
