import math
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
    stopw = stopwords.words('arabic')
    tokens = []
    for w in words:
        if w not in stopw:
            tokens.append(w)
    return tokens


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

    for (a, b, c) in trigram:
        bifinaldic[(a, b)] = math.log(uni_dictionary[a]/len(uni_dictionary)) + math.log(bi_dictionary[(a, b)]/len(bi_dictionary))
        finaldic[(a, b, c)] = math.log(uni_dictionary[a]/len(uni_dictionary)) + math.log(bi_dictionary[(a, b)]/len(bi_dictionary)) + \
                              math.log(tir_dictionary[(a, b, c)]/len(tir_dictionary))
        # finaldic[(a, b, c)] = uni_dictionary[a]/len(uni_dictionary) * bi_dictionary[(a, b)]/len(bi_dictionary) * \
        #                       tir_dictionary[(a, b, c)]/len(tir_dictionary)
    return bifinaldic, finaldic


def test(word, bi, allprops):
    sec_word = ""
    third_word = ""
    prop1 = -1000
    prop2 = -1000
    for (a, b)in bi:
        if a != word:
            continue
        if bi[(a, b)] > prop1:
            prop1 = bi[(a, b)]
            sec_word = b
    sent = word + " " + sec_word
    for (a, b, c) in allprops:
        if a != word or b != sec_word:
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

    x = test("قطاع", bi, allprops)  # enter the test word
    print(x)





