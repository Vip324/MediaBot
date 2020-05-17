import requests
from bs4 import BeautifulSoup
from src import config


def finder_youtube(content):
    """
    Функция поиска по контексту информации в Youtube

    Формат поиска: https://youtube.com/results?search_query=pink+floyd

    :param content: строковое значение
    :return: кортеж словарей(название, полная ссылка, ссылка на изображение)
    """
    BASE_URL = "https://youtube.com"

    spam_search = content.replace(' ', '+')
    url = f'{BASE_URL}/results?search_query={spam_search}&pbj=1'
    response = BeautifulSoup(requests.get(url).text, "html.parser")

    results = []
    rez = response.select('.yt-uix-tile')

    if response.select(".yt-uix-tile"):
        for data in response.select(".yt-uix-tile"):
            spam_src_th = data.find('img').get('data-thumb')
            spam_src_sr = data.find('img').get('src')
            if spam_src_th:
                spam_src = spam_src_th
            else:
                spam_src = spam_src_sr

            data_info = {
                "title": data.find('a', class_='yt-uix-tile-link').get('title'),
                "link": BASE_URL + data.find('a', class_='yt-uix-tile-link').get('href'),
                "img": spam_src
            }
            results.append(data_info)

    return results


def finder_ivi(content):
    """
    Функция поиска по контексту информации в IVI

    Формат поиска: https://www.ivi.ru/search/?q=pink+floyd

    :param content: строковое значение
    :return: кортеж словарей(название, полная ссылка, ссылка на изображение)
    """
    BASE_URL = "https://www.ivi.ru"

    spam_rez = {'title': '', 'link': '', 'src': ''}
    results = []
    spam_search = content.replace(' ', '+')

    url = f"{BASE_URL}/search/?q={spam_search}"
    response = BeautifulSoup(requests.get(url).text, "html.parser")
    if response.find('div', class_='gallery'):
        rez = response.find(
            'div', class_='gallery').find_all(
            'a', class_='nbl-slimPosterBlock')

        for data in rez:
            spam_rez['title'] = f"{data.find('div', class_='nbl-slimPosterBlock__title').text}"
            spam_rez['link'] = f"https://www.ivi.ru{data.get('href')}"
            spam_rez['img'] = data.find('img').get('src')
            results.append(spam_rez)

    return results


def name():
    return None


def photo():
    return None


def output():
    return None


def full_output():
    return None


def parser_text(param):
    return None


if __name__ == '__main__':

    # тестовые запросы:
    # print(finder_youtube('abba the winner takes it all'))
    # print(finder_youtube('fhjj sdfkjkj'))
    print(finder_ivi('pink floyd'))
    # print(finder_ivi('fhjj sdfkjkj'))
