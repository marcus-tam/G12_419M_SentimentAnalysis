from COSC419_fileProcess import process_original_data,syns_process,get_frequent_keyword
from svm import svm
from sklearn.metrics import plot_confusion_matrix



# process_original_data("trainMCD.txt","trainMCD_new.txt")
# process_original_data("testMCD.txt","testMCD_new.txt")
# syns_process("trainMCD_new.txt","trainMCD_new.txt")
# get_frequent_keyword("trainMCD_new.txt" ,"MCD_frequent.txt")
# svm, test_X, test_y = svm("2020-12-09","MCD","trainMCD_new.txt","MCD_frequent.txt","testMCD_new.txt")

# process_original_data("trainRedditMCD.txt","trainRedditMCD_new.txt")
# process_original_data("testRedditMCD.txt","testRedditMCD_new.txt")
# syns_process("trainRedditMCD_new.txt","trainRedditMCD_new.txt")
# get_frequent_keyword("trainRedditMCD_new.txt" ,"RedditMCD_frequent.txt")
# svm("2020-12-09","MCD","trainRedditMCD_new.txt","RedditMCD_frequent.txt","testRedditMCD_new.txt")

# process_original_data("trainBRKB.txt","trainBRKB_new.txt")
# process_original_data("trainPFE.txt","trainPFE_new.txt")
# process_original_data("trainAMZN.txt","trainAMZN_new.txt")
# process_original_data("testAAPL.txt","testAAPL_new.txt")
# process_original_data("testBRKB.txt","testBRKB_new.txt")
# process_original_data("testPFE.txt","testPFE_new.txt")
# process_original_data("testAMZ N.txt","testAMZN_new.txt")
# process_original_data("testAMZN.txt","testAMZN_new.txt")


# pcm = plot_confusion_matrix(svm, test_X, test_y, values_format = 'd', display_labels=['Bullish', 'Bearish'])
# print(pcm.confusion_matrix)

# process_original_data("trainAAPL.txt","trainAAPL_new.txt")
# process_original_data("testAAPL.txt","testAAPL_new.txt")
# syns_process("trainAAPL_new.txt","trainAAPL_new.txt")
# get_frequent_keyword("trainAAPL_new.txt" ,"AAPL_frequent.txt")
# svm("2020-12-09","AAPL","trainAAPL_new.txt","AAPL_frequent.txt","testAAPL_new.txt")

# process_original_data("testBRK.B.txt","testBRKB_new.txt")
# process_original_data("trainBRK.B.txt","trainBRKB_new.txt")
# syns_process("trainBRKB_new.txt","trainBRKB_new.txt")
# get_frequent_keyword("trainBRKB_new.txt" ,"BRKB_frequent.txt")
# svm, test_X, test_y = svm("2020-12-09","BRK-B","trainBRKB_new.txt","BRKB_frequent.txt","testBRKB_new.txt")
# pcm = plot_confusion_matrix(svm, test_X, test_y, values_format = 'd', display_labels=['Bullish', 'Bearish'])
# print(pcm.confusion_matrix)

# f = open('trainRedditMCD.txt', 'r')
# file_contents = f.read()
# print (file_contents)
# f.close()

# syns_process("trainPFE_new.txt","trainPFE_new.txt")
# get_frequent_keyword("trainPFE_new.txt" ,"PFE_frequent.txt")
# svm("2020-12-09","PFE","trainPFE_new.txt","PFE_frequent.txt","testPFE_new.txt")


# process_original_data("testAMZN.txt","testAMZN_new.txt")
# process_original_data("trainAMZN.txt","trainAMZN_new.txt")
# syns_process("trainAMZN_new.txt","trainAMZN_new.txt")
get_frequent_keyword("trainAMZN_new.txt" ,"AMZN_frequent.txt")
# svm("2020-12-09","AMZN","trainAMZN_new.txt","AMZN_frequent.txt","testAMZN_new.txt")
