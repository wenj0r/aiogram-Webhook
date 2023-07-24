from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from create_bot import bot, dp

from dotenv import load_dotenv
from os import getenv

from time import sleep
from asyncio import sleep as asleep

# Загружаем из окружения адрес http тунеля и токен
load_dotenv()
TOKEN = getenv('TOKEN')
DOMAIN_URL = "https://" + getenv('VERCEL_URL')

# URL будет примерно таким https://telegram-webhook-8e67.vercel.app/bot/6387431111:AAFp8QykDUr1wVwqBvKCOBnUENVEg1oIha4
WEBHOOK_PATH = f"/bot"
WEBHOOK_URL = f"{DOMAIN_URL}{WEBHOOK_PATH}"
skip_updates = True

app = FastAPI()


# Устанавливает WEBHOOK URL при запуске
@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    # Реализация skip_updates
    if skip_updates:
        await bot.delete_webhook(drop_pending_updates=True)
        sleep(1) # Без задержки приложение ложится
        await asleep(0)
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


# Доставляет изменения боту при получении POST запроса от Telegram API
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


# Закрывает сессию бота и удаляет вебхук
@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    session = await bot.get_session()
    await session.close()

    # Если используется Redis
    # await dp.storage.close()
    # await dp.storage.wait_closed()


"""
Запускаем работу бота через Web Сервер Unicorn
uvicorn main:app --reload
Флаг --reload перезапускает сервер при каждом изменении и сохранении кода
"""