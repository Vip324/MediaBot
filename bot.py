import telebot
import time
import logger
from src import config
from src import parser
from telebot import types

bot = telebot.TeleBot('1224068014:AAGCOs8lO6eFb2VZBQwP49buOR3PfRfUAP8')
spam_response = {}  # Временная переменная хранит возвращаемые парсером данные


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, config.START_MSG)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, config.HELP_MSG)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    def show_parser(parser, film_source):
        response, photo = parser[film_source]['title'], parser[film_source]['img']
        if photo is not None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="[​​​​​​​​​​​]({}) {}".format(photo, response), parse_mode='markdown',
                                  reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=response, reply_markup=keyboard)

    if call.message:
        if call.data == "show_more":
            callback_button = types.InlineKeyboardButton(
                text="Коротко", callback_data="show_less")
            watch_button = types.InlineKeyboardButton(
                text="Смотреть онлайн", callback_data="watch")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            keyboard.add(watch_button)

            # Выводим два варианта поиска
            if spam_response != {}:
                #
                if spam_response['parser_ivi'] != '':
                    show_parser(spam_response, 'parser_ivi')
                if spam_response['parser_youtube'] != '':
                    show_parser(spam_response, 'parser_youtube')
            response, photo = spam_response['parser_ivi']['title'], spam_response['parser_ivi']['img']
            if photo is not None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="[​​​​​​​​​​​]({}) {}".format(photo, response), parse_mode='markdown',
                                      reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=response, reply_markup=keyboard)

        if call.data == "watch":
            back_button = types.InlineKeyboardButton(
                text="Назад", callback_data="show_less")
            ivi_button = types.InlineKeyboardButton(
                text="IVI", url=spam_response['parser_ivi']['link'])
            youtube_button = types.InlineKeyboardButton(
                text="Youtube", url=spam_response['parser_youtube']['link'])

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(back_button)
            if spam_response['parser_ivi']['link'] != '':
                keyboard.add(ivi_button)
            if spam_response['parser_youtube']['link'] != '':
                keyboard.add(youtube_button)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=config.WATCH_MSG, reply_markup=keyboard)


# Проверка бота жив или нет

@bot.message_handler(content_types=["text"])
def handle_text(message):
    spam_response = {}
    # print(type(message.json['text']))
    spam_response = parser.parser_text(message.json['text'])
    # print(spam_response)

    if spam_response['parser_youtube'] != '':
        response = spam_response['parser_youtube']
        bot.send_message(message.chat.id, 'We found on YouTube:')
        bot.send_message(message.chat.id, response['title'])
    if spam_response['parser_ivi'] != '':
        response = spam_response['parser_ivi']
        bot.send_message(message.chat.id, 'We found on IVI:')
        bot.send_message(message.chat.id, response['title'])


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, )
        except Exception as one:
            logger.error(one)
            time.sleep(15)
