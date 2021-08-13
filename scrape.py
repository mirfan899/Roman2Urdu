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


# text = "بنگلہ دیش کی عدالتِ عالیہ نے طلاق کے ایک مقدمے کا فیصلہ کرتے ہوئے علما کے فتووں کو غیر قانونی قرار دیا ہے۔ عدالت نے پارلیمنٹ سے یہ درخواست کی ہے کہ وہ جلد ایسا قانون وضع کرے کہ جس کے بعد فتویٰ بازی قابلِ دست اندازیِ پولیس جرم بن جائے۔ بنگلہ دیش کے علما نے اس فیصلے پر بھر پور ردِ عمل ظاہرکرتے ہوئے اس کے خلاف ملک گیر تحریک چلانے کا اعلان کیا ہے۔ اس ضمن میں علما کی ایک تنظیم ”اسلامک یونٹی الائنس“ نے متعلقہ ججوں کو مرتد یعنی دین سے منحرف اور دائرۂ اسلام سے خارج قرار دیا ہے۔"
#
# results = ijunoon(get_transliteration(text))

