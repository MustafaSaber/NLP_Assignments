import globals
from gensim.models import doc2vec
from collections import namedtuple
import numpy as np


class DocumentToVector:
    analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.splitvalue = int(0.75 * len(y))
        self.run()

    def load_data(self):
        docs = []
        for i, text in enumerate(self.x):
            words = text.lower().split()
            tags = [i]
            docs.append(self.analyzedDocument(words, tags))
        return doc2vec.Doc2Vec(docs, vector_size=100, window=10, min_count=2, workers=4)

    def change_data(self, trained_model):
        return [trained_model.docvecs[i] for i in range(len(self.x))]

    def split(self, data_to_split):
        return data_to_split[:self.splitvalue], data_to_split[self.splitvalue:], \
               self.y[:self.splitvalue], self.y[self.splitvalue:]

    def new_document_prediction(self, text, trained_model):
        val = [trained_model.infer_vector(text.split()) for text in text]
        val = np.array(val)
        return globals.logistic_regression.predict(val)

    def run(self):
        model = self.load_data()
        new_x = self.change_data(model)
        x_train, x_test, y_train, y_test = self.split(new_x)
        globals.model_train(x_train, y_train, x_test, y_test)
        text_to_predict = ["This is a bad movie", "This is a good movie"]
        ans = self.new_document_prediction(text_to_predict, model)
        print(f"The predicted Label is: {ans}")
        globals.plot(x_train, y_train)

