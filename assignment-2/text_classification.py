from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from load_data import get_data
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def set_matrices(x, y, to_split, vectroizer_used):
    y_train, y_test = y[:to_split], y[to_split:]
    x_train, x_test = x[:to_split], x[to_split:]

    x_train, x_test = vectroizer_used.fit_transform(x_train), vectroizer_used.transform(x_test)
    return x_train, y_train, x_test, y_test


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

    tfid = TfidfVectorizer(lowercase=True, analyzer='word', stop_words='english')
    x_train, y_train, x_test, y_test = set_matrices(x, y, int(0.75 * len(y)), tfid)

    logistic_regression = LogisticRegression(C=1e7)
    logistic_regression.fit(x_train, y_train)
    predicted = logistic_regression.predict(x_test)

    print(f"Accuracy score: {accuracy_score(y_test, predicted)}")

    text_to_predict = ["This is a very bad movie", "This is a very good movie"]

    ans = predict(text_to_predict, logistic_regression, tfid)
    print(f"The predicted Label is: {ans}")

    plot(x_train, y_train)


if __name__ == "__main__":
    main()
