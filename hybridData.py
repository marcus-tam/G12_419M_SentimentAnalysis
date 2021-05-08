import pandas as pd

def combinedData(twits_path, red_path, use, symbol):
    twits = (pd.read_csv(twits_path, sep = "\t", header = None)).drop([3], axis = 1)
    red = pd.read_csv(red_path, sep = "\t", header = None)
    combo = twits.append(red)
    path = use + symbol + "Combination.txt"
    combo.to_csv(path, sep = "\t", header = None, index = False)

if __name__=='__main__':
    combinedData("testMCD.txt","testRedditMCD.txt", "test", "MCD")

