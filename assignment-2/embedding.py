import globals
from sklearn.metrics import accuracy_score


class Embedding:
    dic = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.splitvalue = int(0.75 * len(y))
        self.loadfile()
        self.run("SUM")
        self.run("AVG")

    def loadfile(self):
        # Mostafa path /Users/mostafasaber/Desktop/tempNLP/glove.6B/glove.6B.100d.txt
        # Nour path /C:\\Users\Wahba\Desktop\glove.6B.100d.txt
        lines = open("/Users/mostafasaber/Desktop/tempNLP/glove.6B/glove.6B.100d.txt", encoding="utf-8").readlines()
        for i in lines:
            values = i.split()
            self.dic[values[0]] = list(map(float, values[1:]))
        return self.dic

    def change_data(self, value, aggregate):
        list_of_vectors = []
        for text in value:
            words = text.lower().split()
            temp_list_of_vectors = [self.dic[word] if word in self.dic else [0]*100 for word in words]
            temp_list = [sum(t) / len(t) if aggregate == "AVG" else sum(t) for t in zip(*temp_list_of_vectors)]
            list_of_vectors.append(temp_list)
        return list_of_vectors

    def split(self, data_to_split):
        return data_to_split[:self.splitvalue], data_to_split[self.splitvalue:], \
               self.y[:self.splitvalue], self.y[self.splitvalue:]

    def model_train(self, x_train, y_train, x_test, y_test):
        globals.logistic_regression.fit(x_train, y_train)
        predicted = globals.logistic_regression.predict(x_test)
        print(f"Accuracy score: {accuracy_score(y_test, predicted)}")

    def predict(self, text, aggregate):
        return globals.logistic_regression.predict(self.change_data(text, aggregate))

    def run(self, aggregate):
        new_x = self.change_data(self.x, aggregate)
        x_train, x_test, y_train, y_test = self.split(new_x)
        self.model_train(x_train, y_train, x_test, y_test)
        text_to_predict = ["This is a bad movie", "This is a very good movie"]
        ans = self.predict(text_to_predict, aggregate)
        print(f"The predicted Label is: {ans}")



