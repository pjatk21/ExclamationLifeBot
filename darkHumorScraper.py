import requests
import random
from bs4 import BeautifulSoup

PL_DARK_HUMOR_URL = 'https://kawaly.tja.pl/czarny-humor'
PL_KREMOWKA_URL = 'https://kwejk.pl/tag/cenzopapa/strona/'


class BotScraper:
    def __init__(self):
        self.dark_humor_pl_page = PL_DARK_HUMOR_URL
        self.kremowka_page = PL_KREMOWKA_URL

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

        ## Print the joke in the console
        # print('\n\n' + result)
        return result

    def get_kremowka(self):
        """
        Get a random kremowka message from the Polish website 'kwejk.pl'
            :return: kremowka as an image url
        """
        soup = BeautifulSoup(requests.get(self.kremowka_page + str(random.randint(1, 3))).text, 'html.parser')

        kremowki = [kremowka['src'] for kremowka in soup.find_all('img', class_='full-image')]

        kremowka = random.choice(kremowki)
        while kremowka is None:
            kremowka = random.choice(kremowki)

        return kremowka
