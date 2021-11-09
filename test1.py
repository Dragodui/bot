import requests
from bs4 import BeautifulSoup

URL = 'https://kttc.ru/wot/ru/user/Matvey_0001/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.91'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', 'main_stat_table')
    print(items)

html = get_html(URL)
get_content(html.text)
