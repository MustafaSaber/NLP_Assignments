from load_data import get_data
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from tf_idf import TfIdf
from embedding import Embedding
import globals


# To write in classes
def plot(x, y):
    # Using Truncated SVD cause it works on sparse matrix which Tf-Idf return
    # reduce to 50 feature then use TSNE
    reduced = TruncatedSVD(n_components=50, random_state=7).fit_transform(x)
    embedded = TSNE(n_components=3).fit_transform(reduced)
    axes = plt.axes()
    axes.scatter(embedded[:, 0], embedded[:, 1], embedded[:, 2], c=y)
    plt.show()


def main():
    x, y = get_data("txt_sentoken")
    #globals.init()
    sum_embedding = Embedding(x, y)


if __name__ == "__main__":
    main()
