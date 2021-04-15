import requests
from datetime import datetime
import traceback
import time
import json
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import io
import os
import string


def download(filename, payload, url, end, limit):
    """
    @filename: directory to store
    @payload: type of paramaters to store in request.get
    @url: where we receieve the data. Tailored for api.pushshift.io
    @end: Hard limit on the range of posts. 
    @limit: Hard limit on amount of posts.
    """
    print(f"Saving to {filename}")
    if(not os.path.exists(filename)):
        print(f"Create new file for {filename}")
        f = open(filename, "x")
    else:
        print(f"Overwriting file for {filename}")
        f = open(filename, "w")
    count = 0
    prev = round(int(datetime.utcnow().timestamp()))
    payload["before"] = prev
  # limit is used to hard cap posts
    while count<limit:
        time.sleep(1)
        r = requests.get(url, headers={'User-Agent': 'UBCO 419M Group 12'}, params=payload)
        try:
            json_data = r.json()
        except json.decoder.JSONDecodeError:
            time.sleep(1)

        if 'data' not in json_data:
            break
        objects = json_data['data']
        if len(objects) == 0:
            break
        for object in objects:
            prev = object['created_utc']-1
            count += 1
            object["body"] = object["body"].replace("\n", " ")
            print(object["body"].strip("\n"), (datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d"), object["subreddit"]))

            body_of_text = str(object["body"].encode(encoding='ascii', errors='ignore').decode()).lower()
            body_of_text = special_char_removal(body_of_text)
            body_of_text = str(stopwords_removal(body_of_text))

            f.write(str(object["id"])+"\t")
            f.write(datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d")+"\t")
            f.write(body_of_text)
            f.write("\n")

        prev = round(prev)
        payload["before"] = prev
        print(f"Submissions parsed: {count}")


def special_char_removal(text):
    result = text.translate(str.maketrans('','', string.punctuation))
    return result


def stopwords_removal(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    result = [i for i in tokens if not i in stop_words]
    temp = ' '
    return str(temp.join(result))


def decorator(end, limit, ticker):
    """
    Decorator function for download
    """
    url_api = "https://api.pushshift.io/reddit/search/comment"
    start = datetime.utcnow()   

    urls = {"SecurityAnalysis", "Finance", "FinancialIndependence", "WallStreetBets", "Options", "Forex", "Investing", "CanadianInvestor", "Stocks", "Stock_Picks", "StockMarket", "RobinHood", "InvestmentClub"}
    newurllist = "" #Used for params, as seen in for loop below

    for url in urls:
        newurllist = newurllist + url +","
    payload = {'q': ticker, 'subreddit':newurllist, 'limit':limit, 'before':round(start.timestamp())}

    filename = f"unfiltered_reddit_{ticker}.txt"
    output_filename = f"filtered_reddit_{ticker}.txt"
    print(f"Begin donwloading from API Pushshift (Reddit Data) || ticker= {ticker}")
    download(filename, payload, url_api, end, limit)
    print("Finished Downloading")

    
# Collection of subreddits to parse through
ticker = {"AAPL", "AMZN", "PFE", "MCD", "BKB.A"}

# Using hard utc value
end = 1607396161
# end = datetime.utcfromtimestamp(end)
limit = 100000

for stock in ticker:
    decorator(end, limit, stock)
