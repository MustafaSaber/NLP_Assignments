from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from load_data import get_data


def main():
    x, y = get_data("/Users/mostafasaber/Desktop/tempNLP/review_polarity/txt_sentoken")

    print(y)



if __name__ == "__main__":
    main()
