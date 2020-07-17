import requests
from bs4 import BeautifulSoup

from src.news_parser import film


def finder_film(content):
    """
    Функция поиска по контексту информации в Youtube

    Формат поиска: https://x-film/results?search_query=pink+floyd

    :param content: строковое значение
    :return: кортеж словарей(название, полная ссылка, ссылка на изображение)
    """
    BASE_URL = "https://x-film.top"

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

    spam_rez = {'title': '', 'link': '', 'image': ''}
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
            spam_rez['image'] = data.find('img').get('src').split('jpg')[0]+'jpg'
            results.append(spam_rez)

    return results


def parser_text(text):
    """
    Функция возвращает первые значения поиска по тексту в x-film
    :param text: текст для поиска
    :return: словарь словарей(название, полная ссылка, ссылка на изображение)
    """
    response = {'parser_film': '','parser_ivi': ''}
    if finder_ivi(text) != []:
         response['parser_ivi'] = finder_ivi(text)[0]
    a = film('lastkey.txt')
    spam_search = a.search_film(text)
    if spam_search != '':
        response['parser_film'] = a.film_info(spam_search)

    return response


if __name__ == '__main__':
    # тестовые запросы:

    print(parser_text('pink floyd'))
