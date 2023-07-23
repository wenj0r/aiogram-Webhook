from aiogram import types, Dispatcher, Bot
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

"""
Поведение бота нужно описывать с помощью обработчиков. Ниже обычный echo для примера.
Специфическую логику работы бота, например рассылку, можно сделать в отдельном файле bot.py и просто подгрузить в main.py
"""

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer('ЮХУУУУ')

