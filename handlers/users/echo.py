from aiogram import types
from loader import dp


# Заперт боту отвечать на сообщения с "/"
@dp.message_handler(content_types=types.ContentType.TEXT)
async def do_echo(message: types.Message):
    text = message.text
    if text and not text.startswith('/'):
        await message.reply(text=text)
