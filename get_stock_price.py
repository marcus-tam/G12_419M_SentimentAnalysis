import yfinance as yf

def get_stock_price(stockname,start):
    ticker = stockname
    msft = yf.Ticker(ticker)
    hist = msft.history(period="max",start=start,interval="1d")
    print(hist)

def get_labeled_data(stockname,start):
    
if __name__=='__main__':
    get_stock_price("PFE","2020-12-08")