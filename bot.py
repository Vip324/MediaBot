import telebot
import time
import logger
from src import config
from src import parser
from telebot import types


bot = telebot.TeleBot('')


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, config.START_MSG)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, config.HELP_MSG)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "show_more":
            callback_button = types.InlineKeyboardButton(
                text="Коротко", callback_data="show_less")
            watch_button = types.InlineKeyboardButton(
                text="Смотреть онлайн", callback_data="watch")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            keyboard.add(watch_button)
            response, photo = parser.full_output, parser.photo
            if photo is not None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="[​​​​​​​​​​​]({}) {}".format(photo, response), parse_mode='markdown',
                                      reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=response, reply_markup=keyboard)
        if call.data == "show_less":
            callback_button = types.InlineKeyboardButton(
                text="Узнать больше", callback_data="show_more")
            watch_button = types.InlineKeyboardButton(
                text="Смотреть онлайн", callback_data="watch")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            keyboard.add(watch_button)
            response, photo = parser.output, parser.photo
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
                text="IVI", url=config.LINK_IVI + parser.name)
            youtube_button = types.InlineKeyboardButton(
                text="Youtube", url=config.LINK_YOUTUBE + parser.name)
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(back_button)
            keyboard.add(ivi_button)
            keyboard.add(youtube_button)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=config.WATCH_MSG, reply_markup=keyboard)

# Проверка бота жив или нет


@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = parser.parser_text(message.json['text'])
    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, )
        except Exception as e:
            logger.error(e)
            time.sleep(15)

bot.polling()
