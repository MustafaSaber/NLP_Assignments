from sklearn.linear_model import LogisticRegression
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

logistic_regression = LogisticRegression(C=1e7)
stemmer = PorterStemmer()
lemmetizer = WordNetLemmatizer()


def plot(x, y):
    reduced = TruncatedSVD(n_components=50, random_state=7).fit_transform(x)
    embedded = TSNE(n_components=2).fit_transform(reduced)
    axes = plt.axes()
    axes.scatter(embedded[:, 0], embedded[:, 1], c=y)
    plt.show()

