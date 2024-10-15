import re
import os
from collections import Counter
import csv
import networkx as nx
import matplotlib.pyplot as plt


def load_text_files(folder_path):
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text += file.read() + " "
    return text


# do sprawdzenia wynikow dla poszczegolnych tekstow
def load_simple_file(folder_path):
    file_name = "text1.txt" # mozna zmieniac
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    else:
        return "File not found."


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

    return key_words


def word_graph(words, limit=100):
    G = nx.Graph()
    limited_words = words[:limit]

    for i in range(len(limited_words) - 1):
        G.add_edge(limited_words[i], limited_words[i+1])

    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.7)  # wieksze k = wieksza odleglosc miedzy wierzcholkami
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=6, font_weight="bold")

    plt.savefig('word_graph.png', format="png")
    plt.close()


# whole_text = load_simple_file("Files")
whole_text = load_text_files("Files")
words = clean(whole_text)
zipf(words)
word_graph(words)

for i in range(1, 6):
    key_words = select_percentage(words, 10*i)
    print("Słowa konieczne do zrozumienia", 10*i, f"% tekstu: {key_words}")

