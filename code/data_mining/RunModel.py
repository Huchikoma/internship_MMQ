import numpy as np
import pandas as pd
from sklearn.utils import shuffle,check_random_state
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from sklearn.utils import check_random_state
# import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.utils.data as data
import torch.nn.functional as F

from bokeh.plotting import figure,output_file,show
from bokeh.embed import components
from bokeh.resources import CDN

df = pd.read_excel('data_mining/DataSet-density.xlsx')
df = shuffle(df,random_state=16)
df = df.reset_index(drop=True)

## # Generate training data
Y_train = []
X_train = []
for row in range(len(df)-5): # leave 5 data for test
    param = list(df.iloc[row][0:-1]) 
    X_train.append(param) 
    Y_train.append(df.iloc[row][-1])

X_train = np.array(X_train).astype(np.float32)
Y_train = np.array(Y_train).astype(np.float32).reshape(-1,1)

## # Generate test data
Y_test = []
X_test = []
for r in range(len(df)-5,len(df)):
    param = list(df.iloc[r][0:-1])
    X_test.append(param)
    Y_test.append(df.iloc[r][-1])

X_test = np.array(X_test).astype(np.float32)
Y_test = np.array(Y_test).astype(np.float32).reshape(-1,1)

## # Scale the data
scaler = MinMaxScaler(feature_range=(0.1,0.9)).fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

## # Define hyperparameters
num_hidden_neurons = 8

## # Build the model
class module(nn.Module):
    def __init__(self, num_hidden_neurons):
        super(module, self).__init__()
        self.fc1 = nn.Linear(3, num_hidden_neurons)
        self.fc2 = nn.Linear(num_hidden_neurons, 1)
        
    def forward(self, X_train):
        X_train = self.fc1(X_train)
        X_train = F.relu(X_train)
        X_train = self.fc2(X_train)
        return X_train
        
        
model = torch.load("data_mining/2018-9-05.pkl")

def draw2pr():
    # get draw data
    
    test_pred = model.forward(torch.from_numpy(X_test))
    train_pred = model.forward(torch.from_numpy(X_train))

    test_y = []
    for test_p in test_pred:
        test_y.append(test_p.item())
    train_y = []
    for train_p in train_pred:
        train_y.append(train_p.item())
    test_x = list(np.arange(1,6,1))
    train_x = list(np.arange(1,28))

    p1 = figure(title="Model Performance on Test Set")
    p1.scatter(test_x,test_y,marker="triangle",fill_color='red',size=10,legend='Predicted value')
    Y_test1 = Y_test.flatten().tolist()
    p1.scatter(test_x,Y_test1,marker="circle",fill_color='green',size=10,legend='Actual value')
    script1,div1 = components(p1,CDN)

    p2 = figure(title="Model Performance on Training Set")
    p2.scatter(train_x,train_y,marker="triangle",fill_color='red',size=10,legend='Predicted value')
    Y_train1 = Y_train.flatten().tolist()
    print("Y_train",Y_train)
    print("Y_train1",Y_train1)
    p2.scatter(train_x,Y_train1,marker="circle",fill_color='green',size=10,legend='Actual value')
    script2,div2 = components(p2,CDN)
    return script1,script2,div1,div2



def mypredict(X_test):
    X_test = scaler.transform(X_test)
    y_pred = model.forward(torch.from_numpy(X_test))
    return y_pred.item()