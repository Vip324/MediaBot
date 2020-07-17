import os.path
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse


class film:
    host = 'https://x-film.top'
    url = 'https://x-film.top/filmy-2020-goda/'
    lastkey = ""
    lastkey_file = ""

    def __init__(self, lastkey_file):
        self.lastkey_file = lastkey_file

        if (os.path.exists(lastkey_file)):
            self.lastkey = open(lastkey_file, 'r').read()
        else:
            f = open(lastkey_file, 'w')
            self.lastkey = self.get_lastkey()
            f.write(self.lastkey['href'])
            f.close()

    def new_film(self):
        r = requests.get(self.url)
        html = BS(r.content, 'html.parser')

        new = []
        # поправил поиск
        items = html.select('.short > .short-text > a')

        for i in items:
            key = self.parse_href(i['href'])
            if (self.lastkey != key):
                new.append(i['href'])

        return new

    def film_info(self, uri):
        link = uri
        r = requests.get(link)
        html = BS(r.content, 'html.parser')
        info = {

            "title": html.select('.ftitle > h1')[0].text,
            "link": link,
            "image": 'https://x-film.top' + html.select('.fposter')[0].find('img')['src'],
        }

        return info

    def download_image(self, url):
        r = requests.get(url, allow_redirects=True)

        a = urlparse(url)
        filename = os.path.basename(a.path)
        open(filename, 'wb').write(r.content)

        return filename

    def get_lastkey(self):
        r = requests.get(self.url)
        html = BS(r.content, 'html.parser')
        # поправил правило поиска
        items = html.select('.short > .short-text > a')

        return self.parse_href(items[0])

    # пока не могу понять зачем это, но чтобы не ломать логику оставил
    def parse_href(self, href):
        return href

    def update_lastkey(self, new_key):
        self.lastkey = new_key

        with open(self.lastkey_file, "r+") as f:
            data = f.read()
            f.seek(0)
            f.write(str(new_key))
            f.truncate()

        return new_key

    def search_film(self, text):
        # преобразование для строки поиска
        spam_text = text.encode('utf-8')
        spam_str = ''
        for i in spam_text:
            spam_str += hex(i)
        spam_str = spam_str.replace('0x', '%')
        spam_url = 'https://x-film.top/index.php?do=search&subaction=' \
                    'search&search_start=0&full_search=0&result_from=1&story=' \
                    + spam_str

        # print(spam_url)
        r = requests.get(spam_url)
        html = BS(r.content, 'html.parser')
        # print(html)

        # проверка на наличие результата поиска и возрат '' или ссылки на страницу фильма
        spam_rez = html.select('.berrors')
        # print(spam_rez[0].text)
        if 'К сожалению, поиск по сайту не дал никаких результатов.' in spam_rez[0].text:
            # print('ничего не найдено')
            search_text_url = ''
        else:
            spam_rez = html.select('.short-text > a')[0]['href']
            # print(spam_rez)
            search_text_url = spam_rez

        return search_text_url


if __name__ == '__main__':
    # тестовые запросы:
    a = film('lastkey.txt')
    print(a.new_film())
    print(a.film_info('https://x-film.top/6556-plenennaya-nyanya-2020.html'))
    print(a.search_film('black and blue'))
    print(a.film_info(a.search_film('black and blue')))
