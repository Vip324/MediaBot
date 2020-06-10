import asyncio
from data import config
from aiogram import Bot, Dispatcher, executor, types
from loader import dp

bot = Bot(token=config.BOT_TOKEN)
bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные

@dp.callback_query_handler(lambda callback_query: True)
async def handler(callback_query: types.CallbackQuery):
    if callback_query.message:
        if callback_query.data == "watch":
            keyboard = types.InlineKeyboardMarkup()
            if bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] != '':
                ivi_button = types.InlineKeyboardButton(
                    text="IVI",
                    url=bot.spam_response['parser_ivi']['link'])
                youtube_button = types.InlineKeyboardButton(
                    text="Youtube",
                    url=bot.spam_response['parser_youtube']['link'])
                keyboard.row(youtube_button, ivi_button)
            elif bot.spam_response['parser_ivi'] == '' and bot.spam_response['parser_youtube'] != '':
                youtube_button = types.InlineKeyboardButton(
                    text="Youtube",
                    url=bot.spam_response['parser_youtube']['link'])
                keyboard.add(youtube_button)
            elif bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] == '':
                ivi_button = types.InlineKeyboardButton(
                    text="IVI",
                    url=bot.spam_response['parser_ivi']['link'],)
                keyboard.add(ivi_button)
            await callback_query.message.answer(chat_id=callback_query.message.chat.id, text=config.WATCH_MSG, reply_markup=keyboard)