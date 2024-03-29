# -*- coding: utf-8 -*-
"""optimizers-comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWCFns8GuBAZZQiJdPXY81UyMeIzI9Wj
"""

#IMPORTING LIBRARIES
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout,Flatten

# Importing Data
(x_train,y_train),(x_test,y_test)=mnist.load_data()

# Data Reshape
x_train=x_train.reshape(x_train.shape[0],28,28,1)
x_test=x_test.reshape(x_test.shape[0],28,28,1)
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255
y_train=tf.keras.utils.to_categorical(y_train)
y_test=tf.keras.utils.to_categorical(y_test)

# Build Optimizer Call
def build_optimizer(op):
  model=tf.keras.Sequential()
  model.add(tf.keras.Input(shape=(28,28,1)))
  model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=1,activation='relu'))
  model.add(tf.keras.layers.MaxPool2D())
  model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=1,activation='relu'))
  model.add(tf.keras.layers.Dropout(0.25))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(128, activation='relu'))
  model.add(tf.keras.layers.Dense(256, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Dense(10, activation='softmax'))
  model.compile(optimizer=op, loss='categorical_crossentropy', metrics=['accuracy'])
  return model

# Comparing Each Optimizer Accuracy
import os, gc
optimizers=['Adam', 'RMSprop','Adadelta', 'Adagrad', 'SGD']
opt_res=[]
model_res=[]
for i in optimizers:
  model=build_optimizer(i)
  print("Accuracy for: ",i)
  print("\n")
  history=model.fit(x_train,y_train, epochs=5, batch_size=64,verbose=1,validation_data=(x_test, y_test))
  print("\n")
  gc.collect()
  model_res.append(history)
  opt_res.append(history.history['accuracy'])

# Plotting Optimizer Accuracy
import matplotlib.pyplot as plt
fully_nested = [list(zip(*[(ix+1,y) for ix,y in enumerate(x)])) for x in opt_res]
names = ['sublist%d'%(i+1) for i in range(len(fully_nested))]
fig = plt.figure(figsize=(15,10))
for l in fully_nested:
  plt.plot(*l)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend(optimizers, fontsize=9, loc = 'upper right', bbox_to_anchor=(1.1, 1.01))
plt.title("Optimizer Performance Comparison", fontsize=25)
plt.show()

"""Adam and RMSprop performed the best in terms of accuracy and loss reduction, with Adam being
slightly better. Adadelta performed poorly, while Adagrad and SGD showed improvement over
epochs but didn’t reach the same level of performance as Adam and RMSprop within the given
epochs.
"""