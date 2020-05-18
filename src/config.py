import string

START_MSG = "Привет, я твой помощник, который поможет тебе найти фильм или сериал который вы ищете \n" \
            "Заблудился, введи /help"
HELP_MSG = "Напиши мне название любого фильма или сериала по-русски или по-английски!\n" \
           "Тебе выпадет список с названиями сериалов\n" \
           "Кликни по любой."
WATCH_MSG = "Приятного просмотра!  🎥🍿"
ERR_MSG = "По запросу \"{}\" ничего не найдено.\n" \
          "Попробуйте теперь написать на русском, если писали на английском и наоборот.\n" \
          "Если все еще не получилось, я не знаю о таком фильме/сериале.\n" \
          "На всякий случай проверьте правильность написания :)"

LINK_IVI = "https://www.ivi.ru"
LINK_YOUTUBE = 'https://youtube.com'

LINK_KINOPOISK = "https://www.kinopoisk.ru/film/"

LINK_HDREZKA = "http://hdrezka.name/index.php?do=search&subaction=search&q="
LINK_BASKINO = "http://baskino.me/index.php?do=search&mode=advanced&subaction=search&story="



def link_kinopoisk(id):
    return LINK_HDREZKA + str(id) + "/watch/"


def err_msg(name):
    return ERR_MSG.format(name)


PUNCTUATION = set(string.punctuation) - set('-')
