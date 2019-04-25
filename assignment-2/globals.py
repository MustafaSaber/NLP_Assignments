from sklearn.linear_model import LogisticRegression


def init():
    global logistic_regression
    logistic_regression = LogisticRegression(C=1e7)
