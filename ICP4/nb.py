import pandas as pd
import numpy as np
import random as rnd
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
sns.set(style="white",color_codes=True)
import matplotlib.pyplot as plt
from sklearn.svm import SVC,LinearSVC
from sklearn.naive_bayes import GaussianNB
train_data=pd.read_csv('glass.csv')
train,test=train_test_split(train_data,test_size=0.3)
train_X=train.drop("Type",axis=1)
train_Y=train['Type']
test_X=train.drop("Type",axis=1)
test_Y=test['Type']
gaussian = GaussianNB()
gaussian.fit(train_X, train_Y)
pred_Y = gaussian.predict(test_X)
print(pred_Y)
print(accuracy_score(train_Y,pred_Y))