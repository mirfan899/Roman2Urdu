from helpers import clean_urdu_sentence, clean_roman_sentence
urdu = open("data/makhzan_urdu.txt", "r").readlines()
roman = open("data/makhzan_roman.txt", "r").readlines()

usentences = clean_urdu_sentence(urdu)
rsentences = clean_roman_sentence(roman)

with open("data/makhzan_urdu_cleaned.txt", "w") as uwriter:
    for line in usentences:
        uwriter.write(line.strip() + "\n")


with open("data/makhzan_roman_cleaned.txt", "w") as rwriter:
    for line in rsentences:
        rwriter.write(line.strip() + "\n")

print("Written Urdu and Roman cleaned files......")
