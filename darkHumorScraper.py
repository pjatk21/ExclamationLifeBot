import requests
import random
from bs4 import BeautifulSoup

PL_DARK_HUMOR_URL = 'https://kawaly.tja.pl/czarny-humor'


class BotScraper:
    def __init__(self):
        self.dark_humor_pl_page = PL_DARK_HUMOR_URL

    def get_dark_joke(self):
        """
        Get a random dark humor message from the Polish website 'kawaly.tja.pl'
        :return: joke as a string
        """
        soup = BeautifulSoup(requests.get(self.dark_humor_pl_page + "?st=" + str(random.randint(1, 6))).text, 'html'
                                                                                                              '.parser')
        jokes = soup.find_all('div', class_='tresc')
        joke = random.choice(jokes)
        result = ''
        for br in joke.find_all("br"):
            br.replace_with("\n")

        for value in joke:
            result += str(value)

        print('\n\n' + result)
        return result
