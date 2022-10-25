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

#you can upload your validation dataset:
X_Valid = np.loadtxt("ValidData.txt")

#JND1 label for Valid dataset:
JND1Validlabel = np.loadtxt("VJND1.txt")

#JND2 label for Valid dataset:
JND2Validlabel = np.loadtxt("VJND2.txt")

#JND3 label for Valid dataset:
JND3Validlabel = np.loadtxt("VJND3.txt")

#Temporal Information of blocks:
ValidTI = np.loadtxt("VTI.txt")

image_size = 64
num_channels = 3
X_Valid = X_Valid.reshape((-1, image_size, image_size, num_channels))
X_Valid.shape
X_Valid = X_Valid.astype('float32')

ValidTI = ValidTI.astype('float32')

#you can upload your test dataset:
X_Test = np.loadtxt("TestData.txt")

#JND1 label for test dataset:
JND1Testlabel = np.loadtxt("TJND1.txt")

#JND2 label for test dataset:
JND2Testlabel = np.loadtxt("TJND2.txt")

#JND3 label for test dataset:
JND3Testlabel = np.loadtxt("TJND3.txt")

#Temporal Information of blocks:
TestTI = np.loadtxt("TTI.txt")

image_size = 64
num_channels = 3
X_Test = X_Test.reshape((-1, image_size, image_size, num_channels))
X_Test.shape
X_Test = X_Test.astype('float32')

TestTI = TestTI.astype('float32')

#Calculating the average and std of TI
MeanTTI=np.mean(TrainTI, keepdims=True)
STDTTI=np.std(TrainTI, keepdims=True)

#Normalization
TrainTI -= MeanTTI
TrainTI /= STDTTI

ValidTI -= MeanTTI
ValidTI /= STDTTI

TestTI -= MeanTTI
TestTI /= STDTTI

#Calculating the average and std of train dataset
Mean=np.mean(X_Train, axis=(0,1,2), keepdims=True)
STD=np.std(X_Train, axis=(0,1,2), keepdims=True)

#Normalization
X_Train -= Mean
X_Train /= STD

X_Valid -= Mean
X_Valid /= STD

X_Test -= Mean
X_Test /= STD

## Trainig JND1 model

checkpoint = ModelCheckpoint(filepath='JND1CNNModel.h5',
                                 monitor='val_loss',
                                 save_best_only=True,
                                 save_weights_only=True,
                                 mode='min')
csv_logger = CSVLogger('JND1CNNModel.csv', append=True, separator=';')

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

history=model.fit([X_Train, TrainTI], JND1Trainlabel,
                  batch_size=128,
                  epochs=1000,
                  validation_data=([X_Valid, ValidTI], JND1Validlabel),
                  callbacks=[checkpoint, csv_logger],
                  shuffle=True,
                  workers=5)

plt.plot(history.history['loss'], label="Training loss")
plt.plot(history.history['val_loss'], label="Validation loss")
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()
plt.show()

## Trainig JND2 model

checkpoint = ModelCheckpoint(filepath='JND2CNNModel.h5',
                                 monitor='val_loss',
                                 save_best_only=True,
                                 save_weights_only=True,
                                 mode='min')
csv_logger = CSVLogger('JND2CNNModel.csv', append=True, separator=';')

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

history=model.fit([X_Train, TrainTI], JND2Trainlabel,
                  batch_size=128,
                  epochs=1000,
                  validation_data=([X_Valid, ValidTI], JND2Validlabel),
                  callbacks=[checkpoint, csv_logger],
                  shuffle=True,
                  workers=5)

plt.plot(history.history['loss'], label="Training loss")
plt.plot(history.history['val_loss'], label="Validation loss")
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()
plt.show()

## Trainig JND3 model

checkpoint = ModelCheckpoint(filepath='JND3CNNModel.h5',
                                 monitor='val_loss',
                                 save_best_only=True,
                                 save_weights_only=True,
                                 mode='min')
csv_logger = CSVLogger('JND3CNNModel.csv', append=True, separator=';')

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

history=model.fit([X_Train, TrainTI], JND3Trainlabel,
                  batch_size=128,
                  epochs=1000,
                  validation_data=([X_Valid, ValidTI], JND3Validlabel),
                  callbacks=[checkpoint, csv_logger],
                  shuffle=True,
                  workers=5)

plt.plot(history.history['loss'], label="Training loss")
plt.plot(history.history['val_loss'], label="Validation loss")
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()
plt.show()

