import globals
import load_data
from sklearn.metrics import accuracy_score


class Embedding:
    dic = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.splitvalue = int(0.75 * len(y))
        self.run()

    def loadfile(self):
        lines = open("/C:\\Users\Wahba\Desktop\glove.6B.100d.txt", encoding="utf-8").readlines()
        for i in lines:
            values = i.split()
            self.dic[values[0]] = list(map(float, values[1:]))
        return self.dic

    def change_data_ave(self, value):
        list_of_vectors = []
        for text in value:
            words = text.lower().split()
            temp_list_of_vectors = [self.dic[word] if word in self.dic else [0]*100 for word in words]
            temp_list = [sum(t) for t in zip(*temp_list_of_vectors)]
            for i in temp_list:
                i/=len(temp_list_of_vectors)
            list_of_vectors.append(temp_list)

        return list_of_vectors

    def change_data_sum(self, value):
        list_of_vectors = []
        for text in value:
            words = text.lower().split()
            temp_list_of_vectors = [self.dic[word] if word in self.dic else [0]*100 for word in words]
            temp_list = [sum(t) for t in zip(*temp_list_of_vectors)]
            for i in temp_list:
                i/=len(temp_list_of_vectors)
            list_of_vectors.append(temp_list)

        return list_of_vectors

    def split(self, data_to_split):
        return data_to_split[:self.splitvalue], data_to_split[self.splitvalue:], \
               self.y[:self.splitvalue], self.y[self.splitvalue:]

    def model_train(self, x_train, y_train, x_test, y_test):
        globals.logistic_regression.fit(x_train, y_train)
        predicted = globals.logistic_regression.predict(x_test)
        print(f"Accuracy score: {accuracy_score(y_test, predicted)}")

    def predictA(self, text):
        return globals.logistic_regression.predict(self.change_data_ave(text))

    def predicts(self, text):
        return globals.logistic_regression.predict(self.change_data_sum(text))

    def ave(self):
        new_x_ave = self.change_data_ave(self.x)
        x_train, x_test, y_train, y_test = self.split(new_x_ave)
        self.model_train(x_train, y_train, x_test, y_test)
        text_to_predict = ["This is a bad movie", "This is a very good movie"]
        ans = self.predictA(text_to_predict)
        print("The average of word embeddings: ")
        print(f"The predicted Label is: {ans}")

    def summ(self):
        new_x_ave = self.change_data_sum(self.x)
        x_train, x_test, y_train, y_test = self.split(new_x_ave)
        self.model_train(x_train, y_train, x_test, y_test)
        text_to_predict = ["This is a bad movie", "This is a very good movie"]
        ans = self.predicts(text_to_predict)
        print("The sum of word embeddings: ")
        print(f"The predicted Label is: {ans}")

    def run(self):
        self.ave()
        self.summ()



