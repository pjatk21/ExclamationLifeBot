import requests
import random
from bs4 import BeautifulSoup

PL_DARK_HUMOR_URL = 'https://kawaly.tja.pl/czarny-humor'
PL_KREMOWKA_URL = 'https://www.google.com/search?q=cenzopapa&newwindow=1&sxsrf=ALiCzsYLEsw9T7OcUHp4HMCeQsUUk9yAEw:1657831101798&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiS9K2Pnvn4AhWKUXcKHfzXDgQQ_AUoAXoECAEQAw&cshid=1657831218038877&biw=2560&bih=1289&dpr=1.5'


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
        Get a random kremowka message from the Polish website 'wykop.pl'
            :return: kremowka as an image url
        """
        soup = BeautifulSoup(requests.get(self.kremowka_page).text, 'html.parser')

        kremowki = soup.find_all('img')
        kremowka = random.choice(kremowki)['src']
        return kremowka
