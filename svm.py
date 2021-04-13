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
def svm(start,company,filename,filename_frequent,filename2):
    print("Doing svm prediction for",company)
    keywords_vectors=bag_of_words(filename,filename_frequent)
    length=len(keywords_vectors[0])-1
    print("size of feature",length)
    stock_prediction=get_stock_price(company,start)
    d=date_difference(start,keywords_vectors[0][length])
    # index=date_difference(stock_prediction[d][0],keywords_vectors[0][length])
    # print(type(index))
    train_X=[]
    train_y=[]
    for i in range(0,len(keywords_vectors)):
        train_X.append(keywords_vectors[i][0:length])
        d=date_difference(start,keywords_vectors[i][length])+1
        # if date_difference(stock_prediction[d][0],keywords_vectors[i][length])==0:
        #     print(date_difference(stock_prediction[d][0],keywords_vectors[i][length]))
        # print(stock_prediction[d][0],keywords_vectors[i][length])
        #     print("date wrong")
        #     return
        temp=[]
        count0=0
        count1=0
        for a in range (0,7):
            if stock_prediction[d+a][2]==1:
                count1+=1
            elif stock_prediction[d+a][2]==0:
                count0+=1
        if count1>count0:
            # print(1)
            temp.append(1)
        else:
            # print(0)
            temp.append(0)

        # temp.append(stock_prediction[d][2])
        train_y.append(stock_prediction[d][2])
    train_X=np.array(train_X)
    train_y=np.array(train_y)

    keywords_vectors=bag_of_words(filename2,filename_frequent)
    length=len(keywords_vectors[0])-1
    d=date_difference(start,keywords_vectors[0][length])
    # index=date_difference(stock_prediction[d][0],keywords_vectors[0][length])
    # print(type(index))
    test_X=[]
    test_y=[]
    for i in range(0,len(keywords_vectors)):
        test_X.append(keywords_vectors[i][0:length])
        d=date_difference(start,keywords_vectors[i][length])+1
        # if date_difference(stock_prediction[d][0],keywords_vectors[i][length])==0:
        #     print(date_difference(stock_prediction[d][0],keywords_vectors[i][length]))
        # print(stock_prediction[d][0],keywords_vectors[i][length])
        #     print("date wrong")
        #     return
        temp=[]
        count0=0
        count1=0
        for a in range (0,7):
            if stock_prediction[d+a][2]==1:
                count1+=1
            elif stock_prediction[d+a][2]==0:
                count0+=1
        if count1>count0:
            # print(1)
            temp.append(1)
        else:
            # print(0)
            temp.append(0)

        # temp.append(stock_prediction[d][2])
        test_y.append(stock_prediction[d][2])
    test_X=np.array(test_X)
    test_y=np.array(test_y)
    # print("Train data size is",train_X.shape)
    # print("Test data size is",test_X.shape)
    

    train_X=scale(train_X)
    test_X=scale(test_X)
    bestacc_linear=0
    bestC_linear=0
    accs=np.zeros(100)
    params=np.zeros(100)
    bestacc_rbf=0
    bestC_rbf=0
    param=110
    rbf_svm=SVC(kernel='rbf',C=param)
    rbf_svm.fit(train_X,train_y)
    predict_y=rbf_svm.predict(test_X)
    acc = accuracy_score(test_y,predict_y)  
    # plot_confusion_matrix(rbf_svm, test_X, test_y, values_format = 'd', display_labels=['Spam', 'Not Spam'])
    # y_pred = rbf_svm.predict(test_X)
    # acc = metrics.accuracy_score(test_y, y_pred)
    print("The accracy is",acc)

    # plt.plot(params, accs)
    # plt.axis([0, 1000, 0.5, 1])
    # plt.show()
    # print("best accuracy is",bestacc_rbf,"with value C=",bestC_rbf)

if __name__=='__main__':
    svm("2020-12-08","PFE","PFE_new.txt","PFE_frequent.txt","")
