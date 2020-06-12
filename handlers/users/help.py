from aiogram import types
from data import config
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(config.HELP_MSG)

