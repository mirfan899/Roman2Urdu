from helpers import ijunoon, get_transliteration

lines = open("data/makhzan.txt", "r").readlines()
roman = open("data/makhzan_roman.txt", "w")
urdu = open("data/makhzan_urdu.txt", "w")

for index, line in enumerate(lines):
    trans = ijunoon(get_transliteration(line.strip()))
    if trans:
        # roman.write(str(index) + " " + trans.strip() + "\n")
        roman.write(trans.strip() + "\n")
        urdu.write(line.strip() + "\n")

roman.close()
urdu.close()
