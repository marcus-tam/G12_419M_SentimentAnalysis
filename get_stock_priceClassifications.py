
import yfinance as yf
from numpy import exp

def sigmoid(x):
    sig = 1 / (1 + exp(-5*x))
    return round(sig)

def get_stock_price(stockname,start):
    ticker = stockname
    msft = yf.Ticker(ticker)
    hist = msft.history(period="max",start=start,interval="1d")
    hist['DailyDiff'] =  hist['Close'] - hist['Open']
    hist['Bull/Bear'] = sigmoid(hist['DailyDiff'])
    print(hist)

    
if __name__=='__main__':
    get_stock_price("PFE","2020-12-08")
