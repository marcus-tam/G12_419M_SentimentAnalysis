from COSC419_fileProcess import getimdb, process_original_data,syns_process,get_frequent_keyword,getCombinedData
from svm import svm


# only need to run once to load data,I have alreay run it, you dont have to run the commented code

# process_original_data("trainMCD.txt","trainMCD_new.txt")
# process_original_data("testMCD.txt","testMCD_new.txt")
# process_original_data("trainAAPL.txt","trainAAPL_new.txt")
process_original_data("trainBRK.B.txt","trainBRKB_new.txt")
# process_original_data("trainPFE.txt","trainPFE_new.txt")
# process_original_data("trainAMZN.txt","trainAMZN_new.txt")
# process_original_data("testAAPL.txt","testAAPL_new.txt")
process_original_data("testBRK.B.txt","testBRKB_new.txt")
# process_original_data("testPFE.txt","testPFE_new.txt")
# process_original_data("testAMZN.txt","testAMZN_new.txt")
# syns_process("trainMCD_new.txt","trainMCD_new.txt")
# get_frequent_keyword("trainMCD_new.txt" ,"MCD_frequent.txt")
# syns_process("trainAAPL_new.txt","trainAAPL_new.txt")
# get_frequent_keyword("trainAAPL_new.txt" ,"AAPL_frequent.txt")
# syns_process("trainBRKB_new.txt","trainBRKB_new.txt")
# get_frequent_keyword("trainBRK.B_new.txt" ,"BRKB_frequent.txt")
# syns_process("trainPFE_new.txt","trainPFE_new.txt")
# get_frequent_keyword("trainPFE_new.txt" ,"PFE_frequent.txt")
# syns_process("trainAMZN_new.txt","trainAMZN_new.txt")
# get_frequent_keyword("trainAMZN_new.txt" ,"AMZN_frequent.txt")


# svm("2020-12-09","MCD","trainMCD_new.txt","MCD_frequent.txt","testMCD_new.txt")
# svm("2020-12-09","AAPL","trainAAPL_new.txt","AAPL_frequent.txt","testAAPL_new.txt")
# svm("2020-12-09","BRK-B","trainBRKB_new.txt","BRKB_frequent.txt","testBRKB_new.txt")
# svm("2020-12-09","PFE","trainPFE_new.txt","PFE_frequent.txt","testPFE_new.txt")
# svm("2020-12-09","AMZN","trainAMZN_new.txt","AMZN_frequent.txt","testAMZN_new.txt")

getCombinedData("BRKB","2020-12-09","trainBRKB_new.txt","BRKB.train")
getCombinedData("BRKB","2020-12-09","testBRKB_new.txt","BRKB.test")
getimdb("BRKB","2020-12-09","trainBRKB_new.txt","imdb.train")
getimdb("BRKB","2020-12-09","testBRKB_new.txt","imdb.test")
