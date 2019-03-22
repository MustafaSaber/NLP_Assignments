import math
from nltk.collocations import ngrams
from nltk.tokenize import RegexpTokenizer


def create_dic(tri_gram):

    def add_to_dictionary(elem, dictionary):
        if elem not in dictionary:
            dictionary[elem] = 1
        else:
            dictionary[elem] += 1

    uni_dictionary, bi_dictionary, tir_dictionary = {}, {}, {}
    for (a, b, c) in tri_gram:
        add_to_dictionary(a, uni_dictionary)
        add_to_dictionary((a, b), bi_dictionary)
        add_to_dictionary((a, b, c), tir_dictionary)
    a, b, c = tri_gram[len(tri_gram) - 1]
    add_to_dictionary(b, uni_dictionary)
    add_to_dictionary(c, uni_dictionary)
    add_to_dictionary((b, c), bi_dictionary)
    return uni_dictionary, bi_dictionary, tir_dictionary


def p(uni_dict, bi_dict, tri_dict, tri_gram):
    finaldic = {}

    uni_total, bi_total, tri_total = 0, 0, 0

    for key, value in uni_dict.items():
        uni_total += value
    bi_total, tri_total = uni_total - 1, uni_total - 2

    for (a, b, c) in tri_gram:
        finaldic[(a, b, c)] = math.log(uni_dict[a]/uni_total) + math.log(bi_dict[(a, b)]/bi_total) + \
                              math.log(tri_dict[(a, b, c)]/tri_total)
    return finaldic


def predict(word, allprops):
    words = word.split()
    max_value = -10000000000
    ans = ""
    for key, value in allprops.items():
        a, b, c = key
        if len(words) == 1:
            if a == words[0] and value > max_value:
                max_value = value
                ans = a + " " + b + " " + c
        elif len(words) == 2:
            if a == words[0] and b == words[1] and value > max_value:
                max_value = value
                ans = a + " " + b + " " + c
    return ans


if __name__ == '__main__':

    # Inside main to deal with it as lambda function,
    # However the PEB-8 won't accept assign a function to a name without a def

    def readfile(filename):
        return ''.join(open(filename, "r").readlines())

    def tokenzdoc(doc):
        return list(RegexpTokenizer(r'\w+').tokenize(doc))

    def ngram(tokens_list, n):
        return list(ngrams(tokens_list, n))

    document = readfile("courps.txt")
    tokens = tokenzdoc(document)
    trigram = ngram(tokens, 3)

    uni, bi, tri = create_dic(trigram)
    all_props = p(uni, bi, tri, trigram)
    print("Enter the test word:")
    t = input()
    x = predict(t, all_props)
    print(f"the predicted value is: {x}")
