from bs4 import BeautifulSoup
import requests


def get_transliteration(paragraph=None):
    url = "https://www.ijunoon.com/transliteration/urdu-to-roman/"
    post_data = {"text": paragraph}

    r = requests.post(url, data=post_data)
    return r


def ijunoon(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    transliterate = soup.find("div", {"id": "ctl00_inpageResult"}).text
    return transliterate
