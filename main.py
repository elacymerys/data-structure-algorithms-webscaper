import requests

from scraper.scraper import Scraper
from parser.parser import CsvParser

BASE_URL = 'https://github.com/bollwarm/DataStructuresAlgorithms'
FILENAME = 'coding-tasks.csv'


if __name__ == '__main__':
    response = requests.get(BASE_URL)
    page = response.content
    CsvParser.parse_to(FILENAME, Scraper.scrape(page))
    print(f'Saved to {FILENAME} file!')
