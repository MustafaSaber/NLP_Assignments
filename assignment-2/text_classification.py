from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from load_data import get_data
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def se_sum_of_we(x):
    lines = open("/Users/mostafasaber/Desktop/tempNLP/glove.6B/glove.6B.100d.txt").readlines()
    dic = {}
    for i in lines:
        values = i.split()
        dic[values[:1]] = list(map(int, values[1:]))
    list_of_vectors = []
    for text in x:
        words = text.lower().split()
        temp_list_of_vectors = [dic[word] for word in words]
        temp_list = [sum(t) for t in zip(*temp_list_of_vectors)]
        list_of_vectors.append(temp_list)
    # list of vectors is the new X
    return list_of_vectors


def tf_idf(x_train, x_test, tfid):
    return tfid, tfid.fit_transform(x_train), tfid.transform(x_test)


def set_matrices(x, y, to_split, algo):
    tfid = TfidfVectorizer(lowercase=True, analyzer='word', stop_words='english')
    y_train, y_test = y[:to_split], y[to_split:]
    x_train, x_test = x[:to_split], x[to_split:]
    if algo == 0:
        vec, x_train, x_test = tf_idf(x_train, x_test, tfid)
        return tfid, x_train, y_train, x_test, y_test
    if algo == 1:
        new_x = se_sum_of_we(x)
        return tfid, new_x[:to_split], y_train, new_x[to_split:], y_test


def predict_tfidf(text, model_used, tf_idf):
    return model_used.predict(tf_idf.transform(text))


def predict_se_sum_of_we(text, model_used):
    return model_used.predict(se_sum_of_we(text))


def predict(text, model_used, tf_idf, algo):
    if algo == 0:
        return predict_tfidf(text, model_used, tf_idf)
    if algo == 1:
        return predict_se_sum_of_we(text, model_used)


def plot(x, y):
    # Using Truncated SVD cause it works on sparse matrix which Tf-Idf return
    # reduce to 50 feature then use TSNE
    reduced = TruncatedSVD(n_components=50, random_state=7).fit_transform(x)
    embedded = TSNE(n_components=3).fit_transform(reduced)
    axes = plt.axes()
    axes.scatter(embedded[:, 0], embedded[:, 1], embedded[:, 2], c=y)
    plt.show()


def main():
    x, y = get_data("/Users/mostafasaber/PycharmProjects/NLP_Laps/txt_sentoken")

    vec, x_train, y_train, x_test, y_test = set_matrices(x, y, int(0.75 * len(y)), 1)

    logistic_regression = LogisticRegression(C=1e7)
    logistic_regression.fit(x_train, y_train)
    predicted = logistic_regression.predict(x_test)

    print(f"Accuracy score: {accuracy_score(y_test, predicted)}")

    text_to_predict = ["This is a great movie", "This is a very good movie"]

    ans = predict(text_to_predict, logistic_regression, vec, 1)
    print(f"The predicted Label is: {ans}")
    # plot(x_train, y_train)


if __name__ == "__main__":
    main()
