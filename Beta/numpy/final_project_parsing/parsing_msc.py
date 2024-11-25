import cfscrape
from selectolax.parser import HTMLParser
import json
import logging
from datetime import datetime

def load_config(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_url(config):
    """
    Формирует URL для поиска на Avito.
    """
    base_url = f"https://www.avito.ru/{config['city']}/kvartiry/prodam/{config['rooms']}-komnatnye"
    # params = config['other_params']
    # price_from = config['price_range']['from']
    # price_to = config['price_range']['to']
    # full_url = f"{base_url}?price_from={price_from}&price_to={price_to}"
    
    # for key, value in params.items():
    #     full_url += f"&{key}={value}"
    
    return base_url

def generate_url_pool(config, room_range):
    """
    Генерирует пул URL на основе диапазона комнат.
    """
    url_pool = []
    for rooms in room_range:
        config['rooms'] = rooms
        url_pool.append(generate_url(config))
    return url_pool

def get_session():
    """
    Пункт 2: cfscrape - библиотека используется для обхода защиты Cloudflare, 
    которая может блокировать запросы, если они выглядят как боты.
    Для её использования пришлось вернуть библиотеку urllib3 до 
    версии == 1.26.6: pip install urllib3==1.26.6    
    """
    session = cfscrape.create_scraper() 
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru,en-US;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    return session


def get_html(url):
    """
    Создается сессия - затем отправляется GET-запрос.
    Проверяется числовое значение запроса и, в случае успеха,
    происходит парсинг html страницы. 
    Был найден атрибут, соответсвующий объектам (товарам).
    """
    session = get_session()  
    response = session.get(url)  
    
    if response.status_code == 200:
        html = response.text
        tree = HTMLParser(html)  
        items = tree.css('div[data-marker="item"]') 
        
        index = 0
        for item in items[:10]:
            index += 1
            # print(f"{index}. {item.css_first('h3').text()}")  
            name, square, floor = item.css_first('h3').text().split(", ")
            print(f"{index}. ", end="")
            print(f"{name}; Площадь: {square}; Этаж: {floor}")
    else: 
        print(f"Error: {response.status_code}")

def main():
    config = load_config('config.json')
    
    rooms_range = [1, 2, 3]
    url_pool = generate_url_pool(config, rooms_range)
    # url = 'https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_wEjANz_YToxOntzOjg6ImZyb21QYWdlIjtzOjc6ImNhdGFsb2ciO312FITcIwAAAA&f=ASgBAgECAkSSA8YQygiAWQFFxpoMHXsiZnJvbSI6MTAwMDAwMCwidG8iOjcwMDAwMDB9&s=104'
    # 3-komnatnye
    
    print("Собранный пул URL:")
    for url in url_pool:
        print(f"URL: {url}")
    
    print("Демонстрация парсинга:")
    if url_pool:
        get_html(url_pool[0])  # Обработка первого URL из пула
    else:
        print("Пул URL пуст.")
    
    
if __name__ == '__main__':
    main()