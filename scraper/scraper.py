from bs4 import BeautifulSoup

from scraper.objects import Topic, Task


class Scraper:
    @staticmethod
    def scrape(page):
        soup = BeautifulSoup(page, 'html.parser')

        h3_tags = soup.find_all('h3')
        p_tags = soup.find_all('p')

        return {
            'topics': [
                Topic(h3.text) for h3 in h3_tags if h3.a is not None
            ],
            'tasks': [
                Task(
                    int(p.text.split(".")[0]),
                    p.text.split(".")[1],
                    p.a.attrs['href']
                ) for p in p_tags if 'dir' in p.attrs and p.attrs['dir'] == 'auto'
            ]
        }
