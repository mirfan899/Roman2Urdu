from bs4 import BeautifulSoup
import requests
import re


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


def clean_urdu_sentence(sentences):
    cleaned = []
    for sentence in sentences:
        text = sentence.replace("\xa0", " ")
        text = text.replace("-", "")
        # text = text.replace("ِ", "-e-")
        # sentence = sentence.replace("؂", "")
        text = re.sub(r"\((.*?)\)", "", text)
        text = re.sub(r"\d+", " ", text)

        # English punctuations
        # text = re.sub(r"""[!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~]+""", " ", text)
        # Urdu punctuations
        text = re.sub(r"[“”؂:؛؟’‘٭ء،]+", " ", text)
        # Arabic numbers
        # text = re.sub("...", ".", text)
        text = re.sub("۔۔۔", "۔", text)
        text = re.sub(r"[٠‎١‎٢‎٣‎٤‎٥‎٦‎٧‎٨‎٩]+", " ", text)
        # text = re.sub(r"[^\w\s]", " ", text)
        # Remove English characters and numbers.
        text = re.sub(r"[a-zA-z0-9]+", " ", text)
        # remove multiple spaces.
        text = re.sub(r" +", " ", text)
        text = text.split(" ")
        # some stupid empty tokens should be removed.
        text = [t.strip() for t in text if t.strip()]
        cleaned.append(" ".join(text))
    return cleaned


def clean_roman_sentence(sentences):
    cleaned = []
    for sentence in sentences:
        text = sentence.replace("\xa0", " ")
        text = text.replace("-", "")
        text = text.replace("ِ", "-e-")
        text = re.sub(r"\((.*?)\)", "", text)
        text = re.sub(r"\d+", " ", text)

        # English punctuations
        text = re.sub(r"""[!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~]+""", " ", text)
        # Urdu punctuations
        text = re.sub(r"[“”؂:؛؟’‘٭ء،]+", " ", text)
        # Arabic numbers
        # text = re.sub("...", ".", text)
        text = re.sub("۔۔۔", "۔", text)
        text = re.sub(r"[٠‎١‎٢‎٣‎٤‎٥‎٦‎٧‎٨‎٩]+", " ", text)
        # text = re.sub(r"[^\w\s]", " ", text)
        # Remove English characters and numbers.
        text = re.sub(r"[a-zA-z0-9]+", " ", text)
        # remove multiple spaces.
        text = re.sub(r" +", " ", text)
        text = text.split(" ")
        # some stupid empty tokens should be removed.
        text = [t.strip() for t in text if t.strip()]
        cleaned.append(" ".join(text))
    return cleaned
