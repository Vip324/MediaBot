from aiogram import types
from data import config
from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(config.START_MSG)
