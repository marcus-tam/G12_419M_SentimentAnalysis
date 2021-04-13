####################################################################
#   Stocktwits data downloader
####################################################################
from tkinter import *
import time
import nltk
import re
import requests
import json
from requests.exceptions import HTTPError

# Method to clean up data
wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')
def normalize_document(tweet):
    # lower case and remove special characters\whitespaces
    tweet = re.sub(r'[^a-zA-Z\s]', '', tweet, re.I|re.A)
    tweet = tweet.lower()
    tweet = tweet.strip()
    # tokenize tweets
    tokens = wpt.tokenize(tweet)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    tweet = ' '.join(filtered_tokens)
    return tweet

if __name__ == '__main__':
    window = Tk()
    window.title('Pull data using stock twits api')
    window.geometry("1000x700")

    # Input for stock symbol
    index_frame = Frame(window, height=10)
    index_frame.pack()
    Label(index_frame, text="Enter Stock Symbol").grid(row=0)
    e1 = Entry(index_frame)
    e1.grid(row=0, column=1)
    textbox = Text(window, height=80, width=120)

    # Method for generating samples
    def generateSamples():
        textbox.delete('1.0', END)
        symbol = e1.get()
        # Create an API request
        url = "https://api.stocktwits.com/api/2/streams/symbol/" + symbol + ".json"

        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            textbox.insert(END, "Request to stock twits API failed. Please check if symbol name is correct and there is active network connection\n")
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:

            # Parse the response
            output = json.loads(response.text);
            for i in range(0, len(output["messages"])):
                id = output["messages"][i]["id"]
                date = output["messages"][i]["created_at"]
                sentimenttext = normalize_document(output["messages"][i]["body"])
                sentiment = ""
                if (output["messages"][i].get("entities") and output["messages"][i]["entities"].get("sentiment") and
                        output["messages"][i]["entities"]["sentiment"].get("basic")):
                    sentiment = output["messages"][i]["entities"]["sentiment"]["basic"]

                textbox.insert(END, "\n\nId: "+str(id))
                textbox.insert(END, "\nDate: "+date)
                textbox.insert(END, "\nUser Provided Sentiment: " + sentiment)
                try:
                    textbox.insert(END, "\nRaw Sentiment Text: " + output["messages"][i]["body"])
                except Exception as err:
                    textbox.insert(END, "\nRaw Sentiment Text: Can't be rendered due to character out of range")
                textbox.insert(END, "\nProcessed Sentiment Text: " + sentimenttext)


    # Method to download data in bulk
    def pulldata():

        # Generates a file path
        symbol=e1.get()
        textbox.delete('1.0', END)
        filename = e4.get()+"\\stocktwits_api_"+symbol+"_data_1.txt"
        file = open(filename, "w+")
        iter = 0

        try:
            numtweets = int(e2.get())
        except Exception as err:
            textbox.insert(END, "\nInvalid number of tweets")
            textbox.update_idletasks()
            return

        # override max_id if you want to start the data download from a different point
        try:
            max_id = int(e3.get())
        except Exception as err:
            textbox.insert(END, "\nInvalid max id")
            textbox.update_idletasks()
            return


        textbox.insert(END, "\nTweets pulling in progress ...")
        textbox.update_idletasks()

        # Loop for automatically downloading
        # Offset for max_is automatically managed
        while (iter < (int(e2.get())/30)):
            iter = iter + 1
            if max_id == 0:
                url = "https://api.stocktwits.com/api/2/streams/symbol/"+symbol+".json"
            else:
                url = "https://api.stocktwits.com/api/2/streams/symbol/"+symbol+".json?max=" + str(max_id)

            try:
                response = requests.get(url)

                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except HTTPError as http_err:
                textbox.insert(END,
                               "Request to stock twits API failed. Please check if symbol name is correct and there is active network connection\n")
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
            except Exception as err:
                print(f'Other error occurred: {err}')  # Python 3.6
            else:
                output = json.loads(response.text)
                print(response.text)
                for i in range(0, len(output["messages"])):
                    id = output["messages"][i]["id"]
                    max_id = id
                    date = output["messages"][i]["created_at"]
                    sentimenttext = normalize_document(output["messages"][i]["body"])
                    sentiment = ""
                    if (output["messages"][i].get("entities") and output["messages"][i]["entities"].get("sentiment") and
                            output["messages"][i]["entities"]["sentiment"].get("basic")):
                        sentiment = output["messages"][i]["entities"]["sentiment"]["basic"]

                    file.write(str(id))
                    file.write("\t")
                    file.write(date)
                    file.write("\t")
                    file.write(sentimenttext)
                    file.write("\t")
                    file.write(sentiment)
                    file.write("\n")
                file.flush()
                time.sleep(20)
        file.close()
        textbox.insert(END, "\nDownloading completed")


    button1 = Button(window, text="Generate Samples", command=generateSamples)
    button1.pack()
    button1.config(width=20)



    index_frame = Frame(window, height=10)
    index_frame.pack(padx=20, pady=10)
    Label(index_frame, text="Num Tweets").grid(row=0)
    Label(index_frame, text="Max Id to override (use default 0)").grid(row=1)
    Label(index_frame, text="Folder for storing data(Ex: C:\\Work)").grid(row=2)
    e2 = Entry(index_frame)
    e3 = Entry(index_frame)
    e4 = Entry(index_frame)
    e2.grid(row=0, column=1)
    e3.grid(row=1, column=1)
    e4.grid(row=2, column=1)
    button2 = Button(window, text="Pull Data", command=pulldata)
    button2.pack()
    button2.config(width=20)

    textbox.pack()
    mainloop()
