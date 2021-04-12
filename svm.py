# used for manipulating directory paths
import os

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
def svm(start,end):
    keywords_vectors=bag_of_words("PFE_new.txt","PFE_frequent.txt")
    length=len(keywords_vectors[0])-1
    print("size of feature",length)
    stock_prediction=get_stock_price("PFE",start)
    d=date_difference(start,keywords_vectors[0][length])
    index=date_difference(stock_prediction[d][0],keywords_vectors[0][length])
    # print(index)
    X=[]
    y=[]
    for i in range(0,len(keywords_vectors)):
        X.append(keywords_vectors[i][0:length])
        d=date_difference(start,keywords_vectors[i][length])+index+1
        # print(stock_prediction[d][0],keywords_vectors[i][length])
        temp=[]
        temp.append(stock_prediction[d][2])
        y.append(stock_prediction[d][2])
    X=np.array(X)
    y=np.array(y)
    print(X.shape)
    print(y.shape)
    train_X,test_X,train_y,test_y=train_test_split(X,y,test_size=0.3)
    train_X=scale(train_X)
    test_X=scale(test_X)
    bestacc_linear=0
    bestC_linear=0
    accs=np.zeros(100)
    params=np.zeros(100)
    bestacc_rbf=0
    bestC_rbf=0
    # for i in range(1,100):
    param=100
    rbf_svm=SVC(kernel='rbf',C=param)
    rbf_svm.fit(train_X,train_y)
    # predict_y=rbf_svm.predict(test_X)
    # acc = accuracy_score(test_y,predict_y)  
    plot_confusion_matrix(rbf_svm, test_X, test_y, values_format = 'd', display_labels=['Spam', 'Not Spam'])
    y_pred = rbf_svm.predict(test_X)
    acc = metrics.accuracy_score(test_y, y_pred)
    print(acc)
        # accs[i]=acc
    #     params[i]=param
    #     if bestacc_rbf<acc:
    #         bestacc_rbf=acc
    #         bestC_rbf=params[i]
    # plt.plot(params, accs)
    # plt.axis([0, 1000, 0.8, 1])
    # plt.show()
    # print("best accuracy is",bestacc_rbf,"with value C=",bestC_rbf)

if __name__=='__main__':
    svm("2020-12-08","2021-04-03")
