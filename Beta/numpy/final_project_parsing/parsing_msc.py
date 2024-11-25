import requests
from bs4 import BeautifulSoup
import time

server = "https://www.cian.ru/cat.php"
params = {
    'currency': 2,
    'deal_type': 'sale',
    'engine_version': 2,
    'maxprice': 5000000,
    'minprice': 1000000,
    'object_type[0]': 1,
    'offer_type': 'flat',
    'region': 1,
    'room1': 1
}

response = requests.get(server, params=params)

try:
    code = response.raise_for_status()
    
    
    print("Ответ от сервера получен успешно.")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    # titles = soup.find_all('h2', class_='title')
    
    # for title in titles:
    #     print(title.text.strip())
        
    # print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ошибка {e}")    
