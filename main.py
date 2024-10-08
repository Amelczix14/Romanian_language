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


    with open("wynik.csv", 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Słowo', 'Wartość', 'Ranga', "Współczynnik"])

        for rang, (word, value) in enumerate(frequency, start=1):
            csv_writer.writerow([word, value, rang, value * rang])

def select_percentage(words,percent):
    word_counter = Counter(words)
    frequency = word_counter.most_common()
    total_words = sum(word_counter.values())
    limit = 0.01 * percent * total_words

    total_occurrences = 0
    key_words = []

    for word, value in frequency:
        key_words.append(word)
        total_occurrences += value
        if total_occurrences >= limit:
            break

    print(f"Słowa konieczne do zrozumienia 10% tekstu: {key_words}")
    return key_words


whole_text = load_text_files("Files")
words = clean(whole_text)
zipf(words)
select_percentage(words,10)

