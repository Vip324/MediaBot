import os.path
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse


class LordFilm:
    host = 'https://max.lordfilm.cx'
    url = 'https://max.lordfilm.cx/novinki-2020/'
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
        # поправил правило поиска
        # items = html.select('.tiles > .items > .item > a')
        items = html.select('.owl-carousel > .th-item > a')

        for i in items:
            key = self.parse_href(i['href'])

            # if (self.lastkey < key):
            if (self.lastkey != key):
                new.append(i['href'])

        return new

    def film_info(self, uri):
        # link = self.host + uri
        link = uri
        r = requests.get(link)
        html = BS(r.content, 'html.parser')

        # parse poster image url
        """Нужно подправить"""
        # poster = re.match(r'background-image:\s*url\((.+?)\)', html.select('.image-film-logo > .th-img')[0]['style'])

        # remove some stuff
        # remels = html.select('.article.article-show > *')
        # for remel in remels:
        #     remel.extract()

        # form data
        info = {
            # "id": self.parse_href(uri),
            "title": html.select('.fleft-desc > h1')[0].text,
            "link": link,
            "image": 'https:'+ html.select('.fleft-img-in > .fposter')[0].find('img')['src'],
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
        # items = html.select('.tiles > .items > .item > a')

        # поправил возврат результата : ссылки
        # return items[0]['href']
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
    a = LordFilm('lastkey.txt')
    print(a.new_film())
    print(a.film_info('https://max.lordfilm.cx/44760-parni-v-majami.html'))
    a.update_lastkey('https://max.lordfilm.cx/44760-parni-v-majami.html')
    # a.download_image('https://max.lordfilm.cx/44760-parni-v-majami.html')
