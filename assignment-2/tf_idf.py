from sklearn.feature_extraction.text import TfidfVectorizer
import globals


class TfIdf:
    tfid = TfidfVectorizer(lowercase=True, analyzer='word', stop_words='english')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.split = int(0.75 * len(y))
        self.run()

    def split_train(self):
        return self.tfid.fit_transform(self.x[:self.split]), self.tfid.transform(self.x[self.split:]),\
               self.y[:self.split], self.y[self.split:]

    def predict(self, text):
        return globals.logistic_regression.predict(self.tfid.transform(text))

    def run(self):
        x_train, x_test, y_train, y_test = self.split_train()
        globals.model_train(x_train, y_train, x_test, y_test)
        text_to_predict = ["This is a bad movie", "This is a very good movie"]
        ans = self.predict(text_to_predict)
        print(f"The predicted Label is: {ans}")
        globals.plot(x_train, y_train)
