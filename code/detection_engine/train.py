# -*- coding: utf-8 -*-
import os
import preprocess
from sklearn.datasets import fetch_kddcup99
from tensorflow.keras.optimizers import SGD
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt


def train(temp_data1, temp_data2):
    # Constructing neural network hierarchical model
    model = Sequential()
    model.add(Dense(40, input_dim=41, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(64, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(36, kernel_initializer='uniform', activation='relu'))
    # The result is mapped to 23 dimensional space by softmax function, and the final goal is divided into 23 categories
    model.add(Dense(23, kernel_initializer='uniform', activation='softmax'))

    sgd = SGD(lr=0.01)
    model.compile(loss='mse', optimizer=sgd, metrics=['accuracy'])

    # Modify the dataset format to avoid loss of accuracy
    # input_data_train_set
    temp_data1 = temp_data1.astype('float64')
    # target_data_train_set
    temp_data2 = temp_data2.astype('float64')

    # train
    model.fit(temp_data1, temp_data2, epochs=12, batch_size=128)
    model.save(weightDir)


if __name__ == '__main__':
    dataset = fetch_kddcup99()
    data = dataset.data
    target_data = dataset.target

    # test
    # print(label)
    # print(len(label))
    # stop = input()

    # Call data preprocessing function
    data = preprocess.preprocess_data(data)
    target_data = preprocess.preprocess_data_target(target_data)

    # Encode one-hot
    # 0-300000 samples are used as the training set
    input_data_train_set = data[0:300000]
    target_data_train_set = target_data[0:300000]
    input_data_test_set = data[300000::]
    target_data_test_set = target_data[300000::]

    # Judge whether the training of the model is completed
    weightDir = './model.h5'
    flag = 0
    if os.path.exists(weightDir) & flag == 1:
        # After training, load the model weight file
        model = load_model(weightDir)
        print('Model is restoring...')
    else:
        # First train
        print('Model is training...')
        train(input_data_train_set, target_data_train_set)

    # Neural network visualization
    # plot_model(model, to_file='./model.png', show_shapes=True)

    # Echo neural network weight
    # model.summary()




