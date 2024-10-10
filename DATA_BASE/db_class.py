from JSON_DATA import JSON_DATA_LOADER
import datetime
import mysql.connector  # Исправленный импорт


class DB_class:
    def __init__(self):
        self.data = JSON_DATA_LOADER.load_config()
        self.host = self.data["host"]
        self.user = self.data["user"]
        self.password = self.data["password"]
        self.database = self.data["database"]

        # Подключение к базе данных
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor(dictionary=True)



    def get_today_birthdays(self):
        today = datetime.datetime.today().strftime('%m-%d')
        query = """
            SELECT telegram_id, name, interests 
            FROM users 
            WHERE DATE_FORMAT(birthday, '%m-%d') = %s AND is_congratulated = FALSE
        """
        self.cursor.execute(query, (today,))
        return self.cursor.fetchall()

    def update_congratulated(self, telegram_id):
        query = "UPDATE users SET is_congratulated = TRUE WHERE telegram_id = %s"
        self.cursor.execute(query, (telegram_id,))
        self.conn.commit()  # Не забудьте сохранить изменения

    def close(self):
        self.cursor.close()
        self.conn.close()

    # def get_interest(self):
    #     birthdays = self.get_today_birthdays()
    #     interests_list = []
    #     for birthday in birthdays:
    #         print(birthday)
    #         interests = birthday.get('interests', None)
    #         if interests:
    #             interests_list.append(interests)
    #     return interests_list



