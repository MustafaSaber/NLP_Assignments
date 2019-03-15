import math

import nltk
from nltk.collocations import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def readfile(filename):
    f = open(filename, "r")
    document = ""
    for line in f:
        document += line
    return document


def tokenzdoc(document):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(document)
    stopw = stopwords.words('english')
    tokens = []
    for w in words:
        if w not in stopw:
            tokens.append(w)
    return tokens


def ngram(tokens, n):
    trigram = ngrams(tokens, n)
    # print("tokens: \n", tokens)
    # print("Brigrams:")
    # for i in bigrams:
    #     print(i)
    # print("trigrams:")
    # for i in trigram:
    #     print(i)
    return list(trigram)


def createdic(trigram):
    uni_dictionary, bi_dictionary, tir_dictionary = {}, {}, {}
    for (a, b, c) in trigram:
        if a not in uni_dictionary:
            uni_dictionary[a] = 1
        else:
            uni_dictionary[a] += 1
        if (a, b) not in bi_dictionary:
            bi_dictionary[(a, b)] = 1
        else:
            bi_dictionary[(a, b)] += 1
        if (a, b, c) not in tir_dictionary:
            tir_dictionary[(a, b, c)] = 1
        else:
            tir_dictionary[(a, b, c)] += 1
    return uni_dictionary, bi_dictionary, tir_dictionary


def p(uni_dictionary, bi_dictionary, tir_dictionary, trigram):
    finaldic = {}
    for (a, b, c) in trigram:
        finaldic[(a, b, c)] = math.log(uni_dictionary[a]/len(uni_dictionary)) + math.log(bi_dictionary[(a, b)]/len(bi_dictionary)) + \
                              math.log(tir_dictionary[(a, b, c)]/len(tir_dictionary))
        # finaldic[(a, b, c)] = uni_dictionary[a]/len(uni_dictionary) * bi_dictionary[(a, b)]/len(bi_dictionary) * \
        #                       tir_dictionary[(a, b, c)]/len(tir_dictionary)
    return finaldic


if __name__ == '__main__':
    document = readfile("labtask1.txt")
    tokens = tokenzdoc(document)
    trigram = ngram(tokens, 3)

    uni_dictionary, bi_dictionary, tir_dictionary = createdic(trigram)
    allprops = p(uni_dictionary, bi_dictionary, tir_dictionary, trigram)
    print(uni_dictionary)
    print(bi_dictionary)
    print(tir_dictionary)
    print(allprops)



