from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data import config
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(message.chat.id, config.START_MSG)
