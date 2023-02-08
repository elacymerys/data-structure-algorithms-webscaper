import requests

from scraper import Scraper

BASE_URL = 'https://github.com/bollwarm/DataStructuresAlgorithms'


if __name__ == '__main__':
    response = requests.get(BASE_URL)
    page = response.content
    print(Scraper.scrape(page))
