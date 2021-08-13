from helpers import ijunoon, get_transliteration

lines = open("data/makhzan.txt", "r").readlines()

transliteration = []
for line in lines:
    transliteration.append(ijunoon(get_transliteration(line.strip())))

with open("data/makhzan_roman.txt", "w") as writer:
    for line in transliteration:
        writer.write(line+"\n")