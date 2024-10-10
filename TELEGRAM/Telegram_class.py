
from telegram import Bot
from JSON_DATA import JSON_DATA_LOADER


class Telegram_class:


    def __init__(self):
        self.data = JSON_DATA_LOADER.load_config()

        self.TELEGRAM_BOT_TOKEN = self.data.get("TELEGRAM_BOT_TOKEN", None)  # Получаем токен
        if not self.TELEGRAM_BOT_TOKEN:
            raise ValueError("Токен бота не найден в конфигурации")
        self.bot = Bot(token=self.TELEGRAM_BOT_TOKEN)  # Создаем объект бота

    async def send_congratulation(self, telegram_id, message):
        try:
            await self.bot.send_message(chat_id=telegram_id, text=message)  # Используем await для асинхронного вызова
            print(f"Поздравление отправлено пользователю {telegram_id}")
        except Exception as e:
            print(f"Ошибка отправки сообщения пользователю {telegram_id}: {e}")
            raise e  # Передаем исключение дальше