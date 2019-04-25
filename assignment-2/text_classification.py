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
    # Mostafa path /Users/mostafasaber/PycharmProjects/NLP_Laps/txt_sentoken
    # Nour path C:\\Users\Wahba\Desktop\\txt_sentoken
    x, y = get_data("/Users/mostafasaber/PycharmProjects/NLP_Laps/txt_sentoken")
    print("MODEL 1 and 2: ")
    Embedding(x, y)
    print("MODEL 3: ")
    TfIdf(x, y)


if __name__ == "__main__":
    main()
