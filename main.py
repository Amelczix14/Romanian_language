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


def clean(text):
    text = re.sub(r'[^a-zA-ZĂăÂâÎîȘșȚț\s-]', '', text)
    text = text.lower()
    words = text.split()
    word_to_remove = "-"
    filtered_words = [word for word in words if word not in word_to_remove]
    return filtered_words

def zipf(words):
    word_counter = Counter(words)
    frequency = word_counter.most_common()

    # print(frequency[:10])

    with open("wynik.csv", 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Słowo', 'Wartość', 'Ranga'])

        for ranga, (word, value) in enumerate(frequency, start=1):
            csv_writer.writerow([word, value, ranga])

whole_text = load_text_files("Files")
words = clean(whole_text)
zipf(words)

# dopisac funkcje liczaca wartosc/range
