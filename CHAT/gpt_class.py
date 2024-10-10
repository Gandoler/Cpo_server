import requests
from JSON_DATA import JSON_DATA_LOADER


class gpt_class:
    def __init__(self):
        self.data = JSON_DATA_LOADER.load_config()
        if self.data:
            self.api_key = self.data.get("CHATIK")  # Ваш ключ API

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
