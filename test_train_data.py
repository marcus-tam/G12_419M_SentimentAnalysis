import numpy as np
import pandas as pd
import datetime

def trainTest(name, cutDateStr, symbol):
    datRaw = pd.read_csv(name, delimiter='\t', header = None) 
    df = pd.DataFrame(datRaw)
    df = df.drop(3,axis = 1) 
    df.columns = ['id','dateStr','tweet']
    df['dateStr'] = df.dateStr.str.slice(0,10)
    df['date'] = pd.to_datetime(df['dateStr'], format="%Y-%m-%d")
    cutDate = datetime.datetime.strptime(cutDateStr, "%Y-%m-%d")
    totalSet = df.loc[df['date'] > cutDate, 'tweet']
    lenTrain = round((totalSet.shape[0]) *0.7)
    trainSet = totalSet.tail(lenTrain)
    trainName = "train"+symbol + ".csv"
    trainSet.to_csv(trainName)
    lenTest = round((totalSet.shape[0])*0.3)
    testSet = totalSet.tail(lenTest)
    testName = "test"+symbol + ".csv"
    testSet.to_csv(testName)


n = 'stocktwitsBRK.B_1.txt' #file name on you local computer
d = '2021-03-23' #Date that wwe are going to cut all the companies at for data synchronicity 
s = 'BRK.B' #symbole of stock, used to name the output file
trainTest(n,d,s)
