import os
from dotenv import load_dotenv
# from PIL import Image

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL_IVI = os.getenv("URL_IVI")
URL_YOUTUBE = os.getenv("URL_YOUTUBE")


admins = [

]

ip = os.getenv("ip")
#
aiogram_redis = {
    'host': ip,
}
#
redis = {
    'adress': (ip, 6379),
    'encoding': 'utf8'
}

START_MSG = "Привет, я твой помощник, который поможет тебе найти фильм или сериал :) \n" \
            "Заблудился, введи /help"
HELP_MSG = "Напиши мне название любого фильма или сериала по-русски или по-английски!\n" \
           "Тебе выпадет список с названиями\n" \
           "Кликни по любой."
SEARCH_MSG = "По Вашему запросу найден:"
WATCH_MSG = "Приятного просмотра!  🎥🍿"
ERR_MSG = "По запросу \"{}\" ничего не найдено.\n" \
          "Попробуйте теперь написать на русском, если писали на английском и наоборот.\n" \
          "Если все еще не получилось, я не знаю о таком фильме/сериале.\n" \
          "На всякий случай проверьте правильность написания :)"
subscribe_MSG = "Поздравляю, Вы подписались!\n" \
                "Ждите, скоро выйдут новые обзоры и вы узнаете о них первыми =)"
unsubscribe_MSG = "Очень жалко, что покинули нас."

# img_subscribe = Image.open('D:\FM_Bot\TelegramBot\TelegramBot\img\subscribe.gif')

def err_msg(name):
    return ERR_MSG.format(name)

