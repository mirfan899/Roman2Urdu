from helpers import ijunoon, get_transliteration

lines = open("data/makhzan_urdu.txt", "r").readlines()
roman = open("data/makhzan_roman.txt", "w")

for line in lines:
    trans = ijunoon(get_transliteration(line.strip()))
    roman.write(trans.strip() + "\n")

roman.close()
