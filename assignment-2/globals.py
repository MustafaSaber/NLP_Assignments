from sklearn.linear_model import LogisticRegression
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

logistic_regression = LogisticRegression(C=1e7)
stemmer = PorterStemmer()
lemmetizer = WordNetLemmatizer()


def plot(x, y):
    reduced = TruncatedSVD(n_components=50, random_state=7).fit_transform(x)
    embedded = TSNE(n_components=2).fit_transform(reduced)
    axes = plt.axes()
    axes.scatter(embedded[:, 0], embedded[:, 1], c=y)
    plt.show()


def model_train(x_train, y_train, x_test, y_test):
    logistic_regression.fit(x_train, y_train)
    predicted = logistic_regression.predict(x_test)
    print(f"Accuracy score: {accuracy_score(y_test, predicted)}")
