from load_data import get_data
from tf_idf import TfIdf
from embedding import Embedding
from document_vector import DocumentToVector


def main():
    # Mostafa path /Users/mostafasaber/PycharmProjects/NLP_Laps/txt_sentoken
    # Nour path C:\\Users\Wahba\Desktop\\txt_sentoken
    x, y = get_data("/Users/mostafasaber/PycharmProjects/NLP_Laps/txt_sentoken")
    print("MODEL 1 and 2: ")
    Embedding(x, y)
    print("MODEL 3: ")
    TfIdf(x, y)
    print("MODEL 4:")
    DocumentToVector(x, y)


if __name__ == "__main__":
    main()
