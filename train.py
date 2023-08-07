from posenet_base import OpenPose, cv2
import argparse
from time import time
import json
import os
import sys
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

#from test_new import *
from preprocessing import *
#from sklearn import metrics
import random
from random import randint
from pyfiglet import Figlet
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.metrics import confusion_matrix
import torch
import json


r=Sequential()

r.add(LSTM(units=25,return_sequences=True,input_shape=(32,28)))
r.add(Dropout(0.2))

r.add(LSTM(units=25,return_sequences=True))
r.add(Dropout(0.2))

r.add(LSTM(units=25,return_sequences=True))
r.add(Dropout(0.2))

r.add(LSTM(units=25,return_sequences=True))
r.add(Dropout(0.2))

r.add(LSTM(units=25,return_sequences=True))
r.add(Dropout(0.50))

r.add(LSTM(units=25,return_sequences=True))
r.add(Dropout(0.2))

r.add(LSTM(units=5))
r.add(Dropout(0.2))

r.add(Dense(units=2))

r.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])

r.fit(X_train,y_train,epochs=100,batch_size=16)     

p=r.predict(X_test)
model_json = r.to_json()
with open("model.json", "w") as json_file:
	json_file.write(model_json)
# serialize weights to HDF5
r.save_weights("weights.h5")