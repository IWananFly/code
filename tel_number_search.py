import multiprocessing
import re
import requests


def tel_number_search(url):
    """Ищет номера телефонов поо заданномоу адресу

    :param url: Просто ссылка страничку для поиска. Подразумевается, что ссылки уже скомпонованы и передаются правильно
    :return:
    """

    pattern = re.compile(
        r'\b8{,1}[\s,-]{,1}[\.\-\(]{,1}\d{3}[\.\-\)]{,1}[\s,-]{,1}\d{3}[\.\-\s]{,1}\d{4}\b|'
        r'\b8{,1}[\s,-]{,1}[\.\-\(]{,1}\d{3}[\.\-\)]{,1}[\s,-]{,1}\d{3}[\.\-\s]{,1}\d{2}[\.\-\s]{,1}\d{2}\b|'
        r'\b\d{3}[\.\-\s]{,1}\d{4}\b|'
        r'\b\d{3}[\.\-\s]{,1}\d{2}[\.\-\s]{,1}\d{2}\b'
    )

    # Иногда без нужного хедера не удаётся парсить, оставлю его тут
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    """По-хорошему надо бы прикрутить сюда проксей и при неудаче запроса делать его по-новому.
    Будем исходить из того, что нас не забанят, ведь мы делаем всего по несколько запросов за большой промежуток времени
    А хороший прокси лист ещё надо где-то найти"""
    r = requests.get(url, headers=headers)

    tel_numbers = pattern.findall(r.text)
    for number in tel_numbers:
        index = tel_numbers.index(number)
        # Удалить всё, кроме чисел
        tel_numbers[index] = re.sub('[^0-9]', '', number)
        # Не хватает кода страны
        if len(tel_numbers[index]) == 10:
            tel_numbers[index] = '8' + tel_numbers[index]
        # Не указан код города
        if len(tel_numbers[index]) == 7:
            tel_numbers[index] = '8495' + tel_numbers[index]
    # Условие было - вывести на экран
    print('Page: %s\nNumbers:%s' % (url, tel_numbers))


def tel_numbers_search(urls):
    """Создаёт пул для парсинга телефонных номеров в списке адресов

    :param urls: - список адресов
    :return:
    """
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(tel_number_search, urls)


if __name__ == '__main__':
    url_list = ['https://masterdel.ru/', 'https://repetitors.info/']
    tel_numbers_search(url_list)
