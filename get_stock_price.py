import yfinance as yf
from numpy import exp
import time
import datetime
from helper import date_difference
def get_stock_price(stockname,start):
    ticker = stockname
    msft = yf.Ticker(ticker)
    hist = msft.history(period="max",start=start,interval="1d")
    price_data=hist.values
    price_date=hist.index
    result=[]
    # print(hist)
    pre_date=start
    for i in range (0,len(price_date)):
        temp=[]
        current_data=price_date[i].strftime('%Y-%m-%d')
        if date_difference(pre_date,current_data)>=2:
            six=(price_date[i-1] +datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            temp.append(six)
            difference=(price_data[i-1][3]-price_data[i][0])/2
            temp.append(difference)
            if difference>0:
                temp.append(0)
            else:
                temp.append(1)
            result.append(temp)
            # print(temp)
            temp=[]
            seven=(price_date[i-1] +datetime.timedelta(days=2)).strftime('%Y-%m-%d')
            temp.append(seven)
            difference= (price_data[i-1][3]-price_data[i][0])/4
            temp.append(difference)
            if difference>0:
                temp.append(0)
            else:
                temp.append(1)
            result.append(temp)
            # print(temp)
            temp=[]
        temp.append(current_data)
        difference=price_data[i][0]-price_data[i][3]
        temp.append(difference)
        if difference>0:
            temp.append(0)
        else:
            temp.append(1)
        result.append(temp)
        pre_date=current_data
    # print(result)
    return result

 


def sigmoid(x):
    sig = 1 / (1 + exp(-5*x))
    return round(sig)

    
if __name__=='__main__':
    get_stock_price("PFE","2020-12-08")
