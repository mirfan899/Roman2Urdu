from bs4 import BeautifulSoup
import requests


def get_transliteration(paragraph=None):
    url = "https://www.ijunoon.com/transliteration/urdu-to-roman/"
    post_data = {"text": paragraph}
    try:
        r = requests.post(url, data=post_data)
        return r
    except:
        print("Issue with response from https://www.ijunoon.com/transliteration/urdu-to-roman/")
        return False


def ijunoon(r):
    if r:
        soup = BeautifulSoup(r.text, 'html.parser')
        transliterate = soup.find("div", {"id": "ctl00_inpageResult"}).text

        return transliterate
    else:
        return None
