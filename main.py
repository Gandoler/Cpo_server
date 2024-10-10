import asyncio
import schedule
from DATA_BASE import db_class
from TELEGRAM import Telegram_class
from CHAT import gpt_class

async def func_cong(DB, GPT, TG):
    try:
        friends = DB.get_today_birthdays()
        print(f"Найдено {len(friends)} пользователей с днём рождения сегодня.")

        for friend in friends:
            interests = (lambda interests: interests if interests else "Придумай ему увлечения")(friend['interests'])
            message_point = str(friend['friend_username'])
            message_text = GPT.generate_congratulation(friend['name'], interests)

            try:
                await TG.send_congratulation(friend['telegram_id'], message_point)
                await TG.send_congratulation(friend['telegram_id'], message_text)

                # DB.update_congratulated(friend['telegram_id'])
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {friend['telegram_id']}: {e}")

        DB.conn.commit()

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        DB.conn.rollback()
    finally:
        DB.close()

async def run_schedule():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

def schedule_congratulations():
    DB = db_class.DB_class()
    GPT = gpt_class.gpt_class()
    TG = Telegram_class.Telegram_class()
    asyncio.create_task(func_cong(DB, GPT, TG))

async def main():
    # Запланировать выполнение каждый день в 9 утра
    schedule.every().day.at("16:57").do(schedule_congratulations)

    # Запуск основного цикла планировщика
    await run_schedule()

if __name__ == "__main__":
    asyncio.run(main())
