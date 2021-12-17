# -*- coding: utf-8 -*-
import preprocess
from keras.models import load_model
from sklearn.datasets import fetch_kddcup99


class NoModelError(Exception):
    def __str__(self):
        row = 'The Model is not exist. Please run python train.py first...'
        return row


class DataError(Exception):
    def __str__(self):
        row = 'Please check your data...'
        return row


if __name__ == '__main__':
    dataset = fetch_kddcup99()
    data = dataset.data
    target_data = dataset.target
    # Data preprocessing
    data = preprocess.preprocess_data(data)
    target_data = preprocess.preprocess_data_target(target_data)

    print(data)
    # Samples after 300000 are used as test sets
    input_data_test_set = data[300000::]
    target_data_test_set = target_data[300000::]

    try:
        # Load model weights file
        model = load_model('./model.h5')
        print('Model is restoring...')
        try:
            input_data_test_set = input_data_test_set.astype('float64')
            target_data_test_set = target_data_test_set.astype('float64')
            loss, accuracy = model.evaluate(input_data_test_set, target_data_test_set, batch_size=128)
            print('Loss:{:f}\nAccuracy:{:f}%'.format(loss, accuracy * 100))
        except:
            raise DataError
    except:
        raise NoModelError