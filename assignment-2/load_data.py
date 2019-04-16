import os
from os import listdir, path
from os.path import isfile, join
import random
reviews = []

# /Users/mostafasaber/Desktop/tempNLP/review_polarity/txt_sentoken


def get_data(path):
    def load_files(path):
        return [file for file in listdir(path) if isfile(join(path, file))]

    pos_reviews = load_files(join(path, "pos"))
    neg_reviews = load_files(join(path, "neg"))

    corpus = []
    for temp_file in pos_reviews:
        text_current_doc = open(join(join(path, "pos"), temp_file)).read()
        corpus.append((text_current_doc, 1))

    for temp_file in neg_reviews:
        text_current_doc = open(join(join(path, "neg"), temp_file)).read()
        corpus.append((text_current_doc, 0))

    random.shuffle(corpus)

    labels = []
    documents = []
    for (value, label) in corpus:
        documents.append(value)
        labels.append(label)

    return documents, labels


# corpus, dict = get_data("/Users/mostafasaber/Desktop/tempNLP/review_polarity/txt_sentoken")

