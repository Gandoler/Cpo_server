import asyncio
from DATA_BASE import db_class
from TELEGRAM import Telegram_class
from CHAT import gpt_class


async def main():
    DB = db_class.DB_class()  # Убедитесь, что вы вызываете конструктор
    GPT = gpt_class.gpt_class()  # Убедитесь, что вы вызываете конструктор
    TG = Telegram_class.Telegram_class()  # Убедитесь, что вы вызываете конструктор
    try:
        users = DB.get_today_birthdays()
        print(f"Найдено {len(users)} пользователей с днём рождения сегодня.")

        for user in users:
            interests = (lambda interests: interests if interests else "Придумай ему увлечения")(user['interests'])
            message = GPT.generate_congratulation(user['name'], interests)
            # message = "C DR"
            try:
                await TG.send_congratulation(user['telegram_id'], message)  # Используйте await для асинхронного вызова
                DB.update_congratulated(user['telegram_id'])
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {user['telegram_id']}: {e}")

        DB.conn.commit()  # Сохраняем изменения через экземпляр DB

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        DB.conn.rollback()  # Откат изменений
    finally:
        DB.close()  # Закрываем соединение

# Запуск основного асинхронного метода
if __name__ == "__main__":
    asyncio.run(main())
