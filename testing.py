from predict import predict
from constants import *
import operator
import pickle


def test():
    count = 0
    test_data = pickle.load(open(BASE_PATH + TESTING_FILE_PATH, "rb"))
    for csong in test_data:
        result = predict(BASE_PATH + test_data[csong].path + ".mp3", 20)
        count += (result[0][0] == test_data[csong].ragam)
        print(result, test_data[csong].ragam)
    print(100 * count / len(test_data))


if __name__ == '__main__':
    test()
