import glob
import xml.etree.ElementTree as ET
from scrape import ijunoon, get_transliteration

xmls = glob.glob("./makhzan/text/*.xml")


for xml in xmls:
    transliteration = []
    tree = ET.parse(xml)
    root = tree.getroot()
    paragraphs = root.find("body/section")
    for p in paragraphs.iter("p"):
        print(p.text)
        transliteration.append(ijunoon(get_transliteration(p.text)))
    with open("data/makhzan.txt", "a") as writer:
        for line in transliteration:
            writer.write(line)
