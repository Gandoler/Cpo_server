import json
import os

def load_config(filename='config.json'):
    """Загружает конфигурацию из файла JSON или создает новый, если файл не существует."""
    # Данные по умолчанию для конфигурации
    default_config = {
        "host": "sql8.freesqldatabase.com",
        "user": "sql8736496",
        "password": "acEaTnWs46",
        "database": "sql8736496",
        "TELEGRAM_BOT_TOKEN": "8182804011:AAG3p5xpywAWD0nNLBgaNvIGg1TC-O7vWY0",
        "CHATIK": "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"
    }

    # Проверяем, существует ли файл
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден. Создаем новый файл с конфигурацией.")
        # Создаем новый файл с конфигурацией
        with open(filename, 'w') as json_file:
            json.dump(default_config, json_file, indent=4, ensure_ascii=False)  # Записываем данные по умолчанию в JSON
            print("Новый файл конфигурации создан.")

    # Загружаем конфигурацию
    try:
        with open(filename, 'r') as json_file:
            config = json.load(json_file)
            print("Конфигурация успешно загружена.")
            return config  # Возвращаем загруженные данные
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON: файл '{filename}' может быть поврежден или неправильно отформатирован.")
        raise ValueError("Ошибка при загрузке конфигурации")  # Добавляем это
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise ValueError("Ошибка при загрузке конфигурации")  # Добавляем это
