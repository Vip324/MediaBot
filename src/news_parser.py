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
        items = html.select('.owl-carousel > .th-item > a')

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
            "image": 'https:'+ html.select('.fposter')[0].find('img')['src'],
            "excerpt": html.select('.fdesc')[0].text[0:300] + '...'
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
        items = html.select('.owl-carousel > .th-item > a')



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


if __name__ == '__main__':
    # тестовые запросы:
    a = film('lastkey.txt')
    print(a.new_film())
    print(a.film_info('https://x-film.top/6556-plenennaya-nyanya-2020.html'))
    a.update_lastkey('https://x-film.top/6556-plenennaya-nyanya-2020.html')

