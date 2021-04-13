#library copied from my own assignment
# used for manipulating directory paths
import os
import torch
# Scientific and vector computation for python
import numpy as np
import metrics
#split data into training and testing set
from sklearn.model_selection import train_test_split
#used for scale data into different range
from sklearn.preprocessing import scale
#to make a support vector machine for classification
from sklearn.svm import SVC
#library to do the cross validation
from sklearn.model_selection import GridSearchCV
#to  view the data graphically
from sklearn.metrics import plot_confusion_matrix
#to calculate the accuracy, will do the match one by one
from sklearn.metrics import accuracy_score
#plot graph
import matplotlib.pyplot as plt
import matplotlib.table as table
# tells matplotlib to embed plots within the notebook
from process_tweets import bag_of_words
from get_stock_price import get_stock_price
from helper import date_difference
def lstm(start,end):
    keywords_vectors=bag_of_words("PFE_new.txt","PFE_frequent.txt")
    length=len(keywords_vectors[0])-1
    print("size of feature",length)
    stock_prediction=get_stock_price("PFE",start)
    d=date_difference(start,keywords_vectors[0][length])
    index=date_difference(stock_prediction[d][0],keywords_vectors[0][length])
    # print(type(index))
    X=[]
    y=[]
    for i in range(0,len(keywords_vectors)):
        X.append(keywords_vectors[i][0:length])
        d=date_difference(start,keywords_vectors[i][length])+index+1
        # if date_difference(stock_prediction[d][0],keywords_vectors[i][length])==0:
        #     print(date_difference(stock_prediction[d][0],keywords_vectors[i][length]))
        #     print(stock_prediction[d][0],keywords_vectors[i][length])
        #     print("date wrong")
        #     return
        temp=[]
        count0=0
        count1=0
        for i in range (0,7):
            if stock_prediction[d][2]==1:
                count1+=1
            elif stock_prediction[d][2]==0:
                count0+=1
        if count1>count0:
            # print(1)
            temp.append(1)
        else:
            # print(0)
            temp.append(0)

        # temp.append(stock_prediction[d][2])
        y.append(stock_prediction[d][2])
    X=np.array(X)
    y=np.array(y)
    input=torch.from_numpy(X)


lstm = torch.nn.LSTM(10, 20,2)#len(X),len(X*2)
input=torch.randn(5,3,10)
# print(input)
h0=torch.randn(2,3,20)
c0=torch.randn(2,3,20)
output,(hn,cn)=lstm(input,(h0,c0))
# print(output)
print(output[:, -1, :])

# print(hn)
# print(cn)
# reset_weigths(lstm)

class TextRNN(nn.Module,length):
  def __init__(self):
    super(TextRNN, self).__init__()
    self.embedding = nn.Embedding(5000, 64) # 进行词嵌入
    self.rnn = torch.nn.LSTM(input_size=length, hidden_size=length, num_layers=2, bidirectional=True)
    self.f1 = nn.Sequential(nn.Linear(256,128),
                nn.Dropout(0.8),
                nn.ReLU())
    self.f2 = nn.Sequential(nn.Linear(128,10),
                nn.Softmax())
  
  def forward(self, x):
    x = self.embedding(x)
    x,_ = self.rnn(x)
    x = F.dropout(x,p=0.8)
    x = self.f1(x[:,-1,:])
    return self.f2(x)