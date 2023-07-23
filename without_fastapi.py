from aiogram.utils.executor import start_webhook
from create_bot import bot, dp

from dotenv import load_dotenv
from os import getenv

# Загружаем из окружения адрес http тунеля и токен
load_dotenv()
TOKEN = getenv('TOKEN')
NGROK_URL = getenv('NGROK_URL')

# URL будет примерно таким https://25d8-94-19-173-17.ngrok-free.app/bot/6387431111:AAFp8QykDUr1wVwqBvKCOBnUENVEg1oIha4
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = f"{NGROK_URL}{WEBHOOK_PATH}"

# Устанавливает WEBHOOK URL при запуске
async def on_startup(dp):
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


# Закрывает сессию бота, чтобы запросы на Webhook больше не приходили
async def on_shutdown(dp):
    await bot.delete_webhook()


"""
Версия без FastApi веб-сервера Uvicorn. Работает только за счет средств Aiogram
"""

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='localhost',
        port=8000
)