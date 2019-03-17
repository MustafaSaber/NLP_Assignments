import math
from nltk.collocations import ngrams
from nltk.tokenize import RegexpTokenizer


def readfile(filename):
    f = open(filename, "r")
    document = ""
    for line in f:
        document += line
    return document


def tokenzdoc(document):
    return list(RegexpTokenizer(r'\w+').tokenize(document))


def ngram(tokens, n):
    trigram = ngrams(tokens, n)
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
    bifinaldic={}
    finaldic = {}

    uni_total, bi_total, tri_total = 0, 0, 0

    for key, value in uni_dictionary.items():
        uni_total += value
    for key, value in bi_dictionary.items():
        bi_total += value
    for key, value in tir_dictionary.items():
        tri_total += value
    # print(str(uni_total) + " " + str(bi_total) + " " + str(tri_total))
    for (a, b, c) in trigram:
        bifinaldic[(a, b)] = math.log(uni_dictionary[a]/uni_total) + math.log(bi_dictionary[(a, b)]/bi_total)
        finaldic[(a, b, c)] = math.log(uni_dictionary[a]/uni_total) + math.log(bi_dictionary[(a, b)]/bi_total) + \
                              math.log(tir_dictionary[(a, b, c)]/tri_total)
        # finaldic[(a, b, c)] = uni_dictionary[a]/len(uni_dictionary) * bi_dictionary[(a, b)]/len(bi_dictionary) * \
        #                       tir_dictionary[(a, b, c)]/len(tir_dictionary)
    return bifinaldic, finaldic


def predict(word, bi, allprops):
    words = word.split(" ")
    sent = ""

    for i in range(len(words)):
        sent += words[i] + " "

    if len(words) == 1:
        sec_word = ""
        prop1 = -1000
        for (a, b) in bi:
            if a != words[0]:
                continue
            if bi[(a, b)] > prop1:
                prop1 = bi[(a, b)]
                sec_word = b
        sent += " " + sec_word
    elif len(words) == 2:
        sec_word = words[1]
    else:
        sec_word = ""

    third_word = ""
    prop2 = -1000
    for (a, b, c) in allprops:
        if a != words[0] or b != sec_word:
            continue
        if allprops[(a, b, c)] > prop2:
            prop2 = allprops[(a, b, c)]
            third_word = c
    sent += " " + third_word
    return sent


if __name__ == '__main__':
    document = readfile("courps.txt")
    tokens = tokenzdoc(document)
    trigram = ngram(tokens, 3)

    uni_dictionary, bi_dictionary, tir_dictionary = createdic(trigram)
    bi, allprops = p(uni_dictionary, bi_dictionary, tir_dictionary, trigram)
    print("Enter the test word:")
    t = input()
    x = predict(t, bi, allprops)
    print(x)





