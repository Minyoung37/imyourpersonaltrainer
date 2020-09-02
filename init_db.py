import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myproject

def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get('https://www.youtube.com/results?search_query=%ED%9E%99%EC%9A%B4%EB%8F%99', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#dismissable > #contents > #items > #items > ytd-video-renderer:nth-child(1)')
    print(trs)
    urls = []
    for tr in trs:
        a = tr.select_one('#video-title > a')
        if a is not None:
            base_url = 'https://serch.youtube.com/'
            url = base_url + a['href']
            urls.append(url)

    print(urls)

    return urls

def insert_youtube(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#video-title > yt-formatted-string').text
    img_url = soup.select_one('#img')['src']
    description_text = soup.select_one(
        '#description-text').text
    print("data")
    doc = {
        'name': name,
        'img_url': img_url,
        'description_text': description_text,
        'url': url,
    }
    db.myproject.insert_one(doc)
    print('완료!', name)


def insert_all():
    db.myproject.drop()
    urls = get_urls()
    for url in urls:
        insert_youtube(url)


insert_all()