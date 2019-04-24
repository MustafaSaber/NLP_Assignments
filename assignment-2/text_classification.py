from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from load_data import get_data
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def set_matrices(x, y, to_split):
    y_train, y_test = y[:to_split], y[to_split:]
    x_train, x_test = x[:to_split], x[to_split:]

    def tf_idf():
        tfid = TfidfVectorizer(lowercase=True, analyzer='word', stop_words='english')
        return tfid, tfid.fit_transform(x_train), tfid.transform(x_test)

    def se_sum_of_we():
        lines = open("/assignment-2/glove.6B.100d.txt").readlines()
        dic = {}
        for i in lines:
            values = i.split()
            dic[values[:1]] = values[1:]

    vec, x_train, x_test = tf_idf()
    return vec, x_train, y_train, x_test, y_test


def predict(text, model_used, vectroizer_used):
    return model_used.predict(vectroizer_used.transform(text))


def plot(x, y):
    # Using Truncated SVD cause it works on sparse matrix which Tf-Idf return
    # reduce to 50 feature then use TSNE
    reduced = TruncatedSVD(n_components=50, random_state=7).fit_transform(x)
    embedded = TSNE(n_components=2).fit_transform(reduced)
    axes = plt.axes()
    axes.scatter(embedded[:, 0], embedded[:, 1], c=y)
    plt.show()


def main():
    x, y = get_data("/Users/mostafasaber/Desktop/tempNLP/review_polarity/txt_sentoken")

    vec, x_train, y_train, x_test, y_test = set_matrices(x, y, int(0.75 * len(y)))

    logistic_regression = LogisticRegression(C=1e7)
    logistic_regression.fit(x_train, y_train)
    predicted = logistic_regression.predict(x_test)

    print(f"Accuracy score: {accuracy_score(y_test, predicted)}")

    text_to_predict = ["This is a great movie", "This is a very good movie"]

    ans = predict(text_to_predict, logistic_regression, vec)
    print(f"The predicted Label is: {ans}")

    # plot(x_train, y_train)


if __name__ == "__main__":
    main()
