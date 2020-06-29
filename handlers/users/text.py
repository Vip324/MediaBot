from data import config
from data.config import WATCH_MSG, SEARCH_MSG
from src import parser
from aiogram import types
from loader import dp, bot
import ffmpeg_streaming

bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные


# общение с ботом
@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message):
    bot.spam_response = {}
    response = '\n'

    # парсим text
    bot.spam_response = parser.parser_text(message['text'])

    # готовим ответ по итогам поиска
    if bot.spam_response['parser_film'] != '':
        # response = response + SEARCH_MSG + '\n' \
        #            + bot.spam_response['parser_film']['title'] + '\n' \
        #            + WATCH_MSG + '\n'
        response = response + WATCH_MSG + '\n'
        await message.answer(bot.spam_response['parser_film']['title'])
        await message.answer_photo(bot.spam_response['parser_film']['image'])
        await message.answer(bot.spam_response['parser_film']['excerpt'])

        # if bot.spam_response['parser_ivi'] != '':
        #     response = response + 'I found on IVI: \n' + bot.spam_response['parser_ivi']['title'] + '\n \n'
        # if bot.spam_response['parser_film'] == '' and bot.spam_response['parser_ivi'] == '':
    if bot.spam_response['parser_film'] == '':
        response = config.ERR_MSG.format(message['text'])

    keyboard = types.InlineKeyboardMarkup()
    watch_button = types.InlineKeyboardButton(text='Просмотр', callback_data='watch')
    keyboard.add(watch_button)
    # video = ffmpeg_streaming.input(['link'])  # загоняем ссылку в обработчик и выводим видео
    # выводим ответ для пользователя с кнопками выбора
    await message.answer(response, reply_markup=keyboard)
