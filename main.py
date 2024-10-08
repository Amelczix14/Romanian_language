import re
import os
from collections import Counter
import csv

def load_text_files(folder_path):
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text += file.read() + " "
    return text


def przetworz_tekst(tekst):
    tekst = re.sub(r'[^a-zA-ZĂăÂâÎîȘșȚț\s-]', '', tekst)
    tekst = tekst.lower()
    slowa = tekst.split()
    word_to_remove = "-"
    filtered_words = [word for word in slowa if word not in word_to_remove]
    return filtered_words

def prawo_zipfa(slowa):
    licznik_slow = Counter(slowa)
    czestosc = licznik_slow.most_common()

    print(czestosc[:10])

    with open("wynik.csv", 'w',newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Słowo', 'Wartość', 'Ranga'])

        for ranga, (slowo, wartosc) in enumerate(czestosc, start=1):
            csv_writer.writerow([slowo, wartosc, ranga])

tekst = load_text_files("Files")
slowa = przetworz_tekst(tekst)
prawo_zipfa(slowa)

#dopisac funkcje liczaca wartosc/range
