import pandas as pd

'''
The dataByDate function takes the combined and preprocessed stocktwits and reddit data as input,
along with the data use (train or test) and the companies symbol, and writes a file that combines 
all the posts associated with one day. We are doing this so that its easier to run the transformer/LSTM.

Note: this should only be ran if the data is to be used in the transformer/LSTM.
'''
def dataByDate(CombinedProcessedData, use, symbol):
    df = pd.read_csv(CombinedProcessedData, sep = "\t", header = None)
    df = df.drop(3,axis = 1) 
    df.columns = ['id','date','post']
    df['date'] = pd.to_datetime(df.date.str.slice(0,10), format="%Y-%m-%d")
    uniDates = pd.DataFrame(df['date'].drop_duplicates())
    uniDates['date'] = pd.to_datetime(uniDates['date'], format="%Y-%m-%d")
    uniDates.insert(1,'posts',"")
    for i in uniDates.index:
        strConcat = ""
        temp = df.loc[df['date'] == uniDates.loc[i,'date'], "post"]
        for j in temp.index:
            if j == max(temp.index):
                strConcat += str(temp.loc[j])
            else:
                strConcat += str(temp.loc[j]) + " "
        uniDates.loc[i,'posts'] = strConcat
    
    path = use + symbol + "ByDate.txt"
    uniDates.to_csv(path, sep = "\t", header = None, index = False)
    print("By date conversion was successful.")

if __name__=='__main__':
    dataByDate("testMCDCombination_new.txt", "test", "MCD")