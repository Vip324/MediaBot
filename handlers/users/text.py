from data import config
from src import parser
from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import api
from loader import dp

bot = Bot(token=config.BOT_TOKEN)
bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные


# общение с ботом
@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message):
    bot.spam_response = {}
    response = '   \n \n'

    # парсим text
    bot.spam_response = parser.parser_text(message.json['text'])

    # готовим ответ по итогам поиска
    if bot.spam_response['parser_youtube'] != '':
        response = response + 'I found on YouTube: \n' + bot.spam_response['parser_youtube']['title'] + '\n \n'
    if bot.spam_response['parser_ivi'] != '':
        response = response + 'I found on IVI: \n' + bot.spam_response['parser_ivi']['title'] + '\n \n'
    if bot.spam_response['parser_youtube'] == '' and bot.spam_response['parser_ivi'] == '':
        response = config.ERR_MSG.format(message.json['text'])

    keyboard = types.InlineKeyboardMarkup()
    watch_button = types.InlineKeyboardButton(text='Просмотр', callback_data='watch')
    keyboard.add(watch_button)

    # выводим ответ для пользователя с кнопками выбора
    await message.answer(message.chat.id, response, reply_markup=keyboard)
