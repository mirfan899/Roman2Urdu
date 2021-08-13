import glob
import xml.etree.ElementTree as ET

xmls = glob.glob("./makhzan/text/*.xml")


for xml in xmls:
    urdu = []
    tree = ET.parse(xml)
    root = tree.getroot()
    paragraphs = root.find("body/section")
    for p in paragraphs.iter("p"):
        urdu.append(p.text)
    with open("data/makhzan_urdu.txt", "a") as writer:
        for line in urdu:
            writer.write(line.strip() +"\n")
