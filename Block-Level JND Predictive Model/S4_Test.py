#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.models import Model, Sequential
import glob
import os
from keras.layers import BatchNormalization, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint, CSVLogger
from keras.layers import (Conv1D, MaxPool1D, Dropout, Flatten, Dense,
                          Input, concatenate)
from keras.models import Model, Sequential

#you can upload your train dataset:
X_Train = np.loadtxt("TrainData.txt")

#JND1 label for train dataset:
JND1Trainlabel = np.loadtxt("JND1.txt")

#JND2 label for train dataset:
JND2Trainlabel = np.loadtxt("JND2.txt")

#JND3 label for train dataset:
JND3Trainlabel = np.loadtxt("JND3.txt")

#Temporal Information of blocks:
TrainTI = np.loadtxt("TI.txt")

image_size = 64
num_channels = 3
X_Train = X_Train.reshape((-1, image_size, image_size, num_channels))
X_Train.shape
X_Train = X_Train.astype('float32')

TrainTI = TrainTI.astype('float32')


#Calculating the average and std of TI
MeanTTI=np.mean(TrainTI, keepdims=True)
STDTTI=np.std(TrainTI, keepdims=True)

#Normalization
TrainTI -= MeanTTI
TrainTI /= STDTTI


#Calculating the average and std of train dataset
Mean=np.mean(X_Train, axis=(0,1,2), keepdims=True)
STD=np.std(X_Train, axis=(0,1,2), keepdims=True)

#Normalization
X_Train -= Mean
X_Train /= STD


#defining the architecture
def network():
    sequence = Input(shape=X_Train.shape[1:], name='Sequence')
    features = Input(shape=(1,), name='Features')
    
    conv = Sequential()
    conv.add(Conv2D(32, (3, 3), padding='same', input_shape=X_Train.shape[1:], activation='relu'))
    conv.add(MaxPooling2D(pool_size=(2, 2)))
    
    conv.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    conv.add(MaxPooling2D(pool_size=(2, 2)))
    
    conv.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    conv.add(MaxPooling2D(pool_size=(2, 2)))
    
    conv.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    conv.add(MaxPooling2D(pool_size=(2, 2)))
    
    conv.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
    conv.add(MaxPooling2D(pool_size=(2, 2)))
    
    conv.add(Flatten())
    part1 = conv(sequence)
    
    merged = concatenate([part1, features])
    
    final = Dense(512, activation='relu')(merged)
    final = Dense(1, activation='relu')(final)
    
    model = Model(inputs=[sequence, features], outputs=[final])

    model.compile(loss='mean_absolute_error', optimizer='adam')
    
    return model

model = network()
model.summary()

opt = keras.optimizers.Adam(learning_rate=0.00001)
model.compile(loss='mean_absolute_error', optimizer=opt)


# In[ ]:


#loading Block-level Data
X_test = np.loadtxt("BlockData.txt")

X_test = X_test.reshape((-1, image_size, image_size, num_channels))
X_test.shape
X_test = X_test.astype('float32')

X_test -= Mean
X_test /= STD

#loading TI of Block-level Data
TestTI = np.loadtxt("BlockLevelTPI.txt")

#loading the trained JND1 model
model.load_weights('JND1CNNModel.h5')
PredictedJND1=model.predict([X_test, TestTI])

#loading the trained JND2 model
model.load_weights('JND2CNNModel.h5')
PredictedJND2=model.predict([X_test, TestTI])

#loading the trained JND3 model
model.load_weights('JND3CNNModel.h5')
PredictedJND3=model.predict([X_test, TestTI])

