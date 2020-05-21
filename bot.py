import telebot
import time
import logger
import json
from src import config
from src import parser
from telebot import types

bot = telebot.TeleBot('1224068014:AAGCOs8lO6eFb2VZBQwP49buOR3PfRfUAP8')
bot.spam_response = {}  # Временная переменная хранит возвращаемые парсером данные


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, config.START_MSG)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, config.HELP_MSG)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    def show_parser(parser, film_source):
        pass
        # response, photo = parser[film_source]['title'], parser[film_source]['img']
        # if photo is not None:
        #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                           text="[​​​​​​​​​​​]({}) {}".format(photo, response), parse_mode='markdown',
        #                           reply_markup=keyboard)
        # else:
        #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                           text=response, reply_markup=keyboard)

    if call.message:
        # if call.data == "show_more":
        #     callback_button = types.InlineKeyboardButton(
        #         text="Коротко", callback_data="show_less")
        #     watch_button = types.InlineKeyboardButton(
        #         text="Смотреть онлайн", callback_data="watch")
        #     keyboard = types.InlineKeyboardMarkup()
        #     keyboard.add(callback_button)
        #     keyboard.add(watch_button)
        #
        #     # Выводим два варианта поиска
        #     if spam_response != {}:
        #         #
        #         if spam_response['parser_ivi'] != '':
        #             show_parser(spam_response, 'parser_ivi')
        #         if spam_response['parser_youtube'] != '':
        #             show_parser(spam_response, 'parser_youtube')
        #     response, photo = spam_response['parser_ivi']['title'], spam_response['parser_ivi']['img']
        #     if photo is not None:
        #         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                               text="[​​​​​​​​​​​]({}) {}".format(photo, response), parse_mode='markdown',
        #                               reply_markup=keyboard)
        #     else:
        #         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                               text=response, reply_markup=keyboard)

        if call.data == "watch":
            keyboard = types.InlineKeyboardMarkup()
            if bot.spam_response['parser_ivi'] != '' and bot.spam_response['parser_youtube'] != '':
                ivi_button = types.InlineKeyboardButton(
                    text="IVI", url=bot.spam_response['parser_ivi']['link'])
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
                    text="IVI", url=bot.spam_response['parser_ivi']['link'])
                keyboard.add(ivi_button)
            bot.send_message(chat_id=call.message.chat.id, text=config.WATCH_MSG, reply_markup=keyboard)


# общение с ботом
@bot.message_handler(content_types=["text"])
def handle_text(message):
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
    bot.send_message(message.chat.id, response, reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
    # while True:
    #     try:
    #         bot.polling(none_stop=True, )
    #     except Exception as one:
    #         logger.error(one)
    #         time.sleep(15)
