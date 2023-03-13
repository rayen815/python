import seaborn as sb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras


data=pd.read_csv("diabetes.csv")
x=data.drop(columns=["Outcome"]).values.reshape(-1,1)
y=data["Outcome"].values.reshape(-1,1)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

model=keras.models.Sequential([
    keras.layers.Dense(500,activation="relu"),
    keras.layers.Dense(200,activation="relu"),
    keras.layers.Dense(75,activation="relu"),
    keras.layers.Dense(2,activation="softmax"),
])
model.compile(optimizer="Adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(xtrain,ytrain,epochs=3)