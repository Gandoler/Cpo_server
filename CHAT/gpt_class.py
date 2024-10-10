import openai
from JSON_DATA import JSON_DATA_LOADER

class gpt_class:
    def __init__(self):
        self.data = JSON_DATA_LOADER.load_config()
        if self.data:  # Проверяем, удалось ли загрузить данные
            openai.api_key = self.data.get("CHATIK")  # Используем get для безопасного извлечения ключа

    def generate_congratulation(self, name, interests):
        prompt = f"Напиши поздравление для {name}, который интересуется {interests}. Поздравление должно быть дружелюбным и теплым."

        response = openai.ChatCompletion.create(
            model="gpt-4o-miniч",  # Указываем актуальную модель
            messages=[
                {"role": "system", "content": "Ты пишешь поздравления для пользователей."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response['choices'][0]['message']['content'].strip()
