# import asyncio
# import logging
# from data import config
# from src import parser
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.bot import api
# from sqlite import SQLighter
# from src.news_parser import LordFilm
# from loader import dp
#
#
#
# logging.basicConfig(level=logging.DEBUG)
# Logger = logging.getLogger(__name__)
#
# # # инициализируем бота
# # bot = Bot(token=config.token)
# # bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные
#
#
# # Подмена базвого URL Для запроса
# PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
# setattr(api, 'API_URL', PATCHED_URL)
#
# # инициализируем соединение с БД
# db = SQLighter('db.db')
#
# # инициализируем парсер
# np = LordFilm('lastkey.txt')
#
# # проверяем наличие новых фильмов и делаем рассылки
# async def scheduled(wait_for):
#     while True:
#         await asyncio.sleep(wait_for)
#
#         # проверяем наличие новых фильмов
#         new_film = np.new_film()
#
#         if (new_film):
#             # если фильмы есть, переворачиваем список и итерируем
#             new_film.reverse()
#             for ng in new_film:
#                 # парсим инфу о новом фильме
#                 nfo = np.film_info(ng)
#
#                 # получаем список подписчиков бота
#                 subscriptions = db.get_subscriptions()
#
#                 # отправляем всем новость
#                 with open(np.download_image(nfo['image']), 'rb') as photo:
#                     for s in subscriptions:
#                         await bot.send_photo(
#                             s[1],
#                             photo,
#                             caption=nfo['title'] + "\n" + "\n" + nfo[
#                                 'excerpt'] + "\n\n" + nfo['link'],
#                             disable_notification=True
#                         )
#
#                     # обновляем ключ
#                 np.update_lastkey(nfo[' '])
#
# # # Команда активации подписки
# # @dp.message_handler(commands=['subscribe'])
# # async def subscribe(message: types.Message):
# #     if (not db.subscriber_exists(message.from_user.id)):
# #         # если юзера нет в базе, добавляем его
# #         db.add_subscriber(message.from_user.id)
# #     else:
# #         # если он уже есть, то просто обновляем ему статус подписки
# #         db.update_subscription(message.from_user.id, True)
# #
# #     await message.answer(
# #         "Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них первыми =)")
# #
# # # Команда отписки
# # @dp.message_handler(commands=['unsubscribe'])
# # async def unsubscribe(message: types.Message):
# #     if (not db.subscriber_exists(message.from_user.id)):
# #         # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
# #         db.add_subscriber(message.from_user.id, False)
# #         await message.answer("Вы итак не подписаны.")
# #     else:
# #         # если он уже есть, то просто обновляем ему статус подписки
# #         db.update_subscription(message.from_user.id, False)
# #         await message.answer("Вы успешно отписаны от рассылки.")
#
# # @dp.callback_query_handler(lambda callback_query: True)
# # async def handler(callback_query: types.CallbackQuery):
# #     if callback_query.message:
# #         if callback_query.data == "watch":
# #             keyboard = types.InlineKeyboardMarkup()
# #             if bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] != '':
# #                 ivi_button = types.InlineKeyboardButton(
# #                     text="IVI",
# #                     url=bot.spam_response['parser_ivi']['link'])
# #                 youtube_button = types.InlineKeyboardButton(
# #                     text="Youtube",
# #                     url=bot.spam_response['parser_youtube']['link'])
# #                 keyboard.row(youtube_button, ivi_button)
# #             elif bot.spam_response['parser_ivi'] == '' and bot.spam_response['parser_youtube'] != '':
# #                 youtube_button = types.InlineKeyboardButton(
# #                     text="Youtube",
# #                     url=bot.spam_response['parser_youtube']['link'])
# #                 keyboard.add(youtube_button)
# #             elif bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] == '':
# #                 ivi_button = types.InlineKeyboardButton(
# #                     text="IVI",
# #                     url=bot.spam_response['parser_ivi']['link'],)
# #                 keyboard.add(ivi_button)
# #             await callback_query.message.answer(chat_id=callback_query.message.chat.id, text=config.WATCH_MSG, reply_markup=keyboard)
#
#
# # # общение с ботом
# # @dp.message_handler(content_types=["text"])
# # async def handle_text(message: types.Message):
# #     bot.spam_response = {}
# #     response = '   \n \n'
# #
# #     # парсим text
# #     bot.spam_response = parser.parser_text(message.json['text'])
# #
# #     # готовим ответ по итогам поиска
# #     if bot.spam_response['parser_youtube'] != '':
# #         response = response + 'I found on YouTube: \n' + bot.spam_response['parser_youtube']['title'] + '\n \n'
# #     if bot.spam_response['parser_ivi'] != '':
# #         response = response + 'I found on IVI: \n' + bot.spam_response['parser_ivi']['title'] + '\n \n'
# #     if bot.spam_response['parser_youtube'] == '' and bot.spam_response['parser_ivi'] == '':
# #         response = config.ERR_MSG.format(message.json['text'])
# #
# #     keyboard = types.InlineKeyboardMarkup()
# #     watch_button = types.InlineKeyboardButton(text='Просмотр', callback_data='watch')
# #     keyboard.add(watch_button)
# #
# #     # выводим ответ для пользователя с кнопками выбора
# #     await message.answer(message.chat.id, response, reply_markup=keyboard)
#
#
#
# # # Заперт боту отвечать на сообщения с "/"
# # @dp.message_handler(content_types=types.ContentType.TEXT)
# # async def do_echo(message: types.Message):
# #     text = message.text
# #     if text and not text.startswith('/'):
# #         await message.reply(text=text)
#
#
#
#
#
#
# if __name__ == '__main__':
#     dp.loop.create_task(scheduled(50))  # пока что оставим 30 секунд (в качестве теста)
#     executor.start_polling(dp, skip_updates=True)
#
