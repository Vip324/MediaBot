from loader import bot, storage, dp
from aiogram.bot import api
from sqlite import SQLighter
from src.news_parser import film
import asyncio
import logging
from aiogram import types
from data import config


logging.basicConfig(level=logging.DEBUG)
Logger = logging.getLogger(__name__)
bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные

# Подмена базвого URL Для запроса
PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


# инициализируем соединение с БД
db = SQLighter('db.db')

# инициализируем парсер
np = film('lastkey.txt')


# проверяем наличие новых фильмов и делаем рассылки
async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        # проверяем наличие новых фильмов
        new_film = np.new_film()

        if new_film:
            # если фильмы есть, переворачиваем список и итерируем
            new_film.reverse()
            for ng in new_film:
                # парсим инфу о новом фильме
                nfo = np.film_info(ng)

                # получаем список подписчиков бота
                subscriptions = db.get_subscriptions()

                # отправляем всем новость
                with open(np.download_image(nfo['image']), 'rb') as photo:
                    for s in subscriptions:
                        await bot.send_photo(
                            s[1],
                            photo,
                            caption=nfo['title'] + "\n" + "\n" + nfo[
                                'excerpt'] + "\n\n" + nfo['link'],
                            disable_notification=True
                        )

                    # обновляем ключ
                np.update_lastkey(nfo[' '])


@dp.callback_query_handler(lambda callback_query: True)
async def handler(callback_query: types.CallbackQuery):
    if callback_query.message:
        if callback_query.data == "watch":
            keyboard = types.InlineKeyboardMarkup()

            # if bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] != '':
            if bot.spam_response['parser_film'] != '':
                # ivi_button = types.InlineKeyboardButton(
                #     text="IVI",
                #     url=bot.spam_response['parser_ivi']['link'])
                film_button = types.InlineKeyboardButton(
                    text="x-film",
                    url=bot.spam_response['parser_film']['link'])
                # keyboard.row(youtube_button, ivi_button)
                keyboard.row(film_button)
            # elif bot.spam_response['parser_ivi'] == '' and bot.spam_response['parser_youtube'] != '':
            elif bot.spam_response['parser_film'] != '':
                film_button = types.InlineKeyboardButton(
                    text="x-film",
                    url=bot.spam_response['parser_film']['link'])
                keyboard.add(film_button)
            # elif bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] == '':
            #     ivi_button = types.InlineKeyboardButton(
            #         text="IVI",
            #         url=bot.spam_response['parser_ivi']['link'],)
            #     keyboard.add(ivi_button)
            await callback_query.message.answer(callback_query.message, text=config.WATCH_MSG, reply_markup=keyboard)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    dp.loop.create_task(scheduled(5000))  # пока что оставим 5000 секунд
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
