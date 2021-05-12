from nltk.corpus import wordnet
import codecs
from get_stock_price import get_stock_price
from helper import date_difference
# centralize the raw data
def process_original_data(filepath_old,filepath_new):
    content=""
    # read old file
    file_old = open(filepath_old,"r")
    count=1
    str=file_old.readline()
    while str!="":
        line_splited=str.split("	")
        if line_splited[len(line_splited)-1]!="\n":
            line_splited[len(line_splited)-1]="\n"
        result="	".join(i for i in line_splited)
        content+=result
        try:
            str=file_old.readline()
        # ignore lines that cannot be read
        except:
            count+=1
            # print (count)
            continue
        count+=1
        
        
    file_old.close()
    #  write new file
    file_new = open(filepath_new, "w")
    file_new.write(content)
    print("Original file process done")
    file_new.close()
#this function is not used for this case
def get_file_dictionary(filepath,filepath_new):
    f=open(filepath,"r",encoding="UTF-8", errors="ignore")
    str=f.readline()
    count=1
    # list of word sort by first character
    keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    while str!="":
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        for word in word_list:
            if_exist=False
            if len(word)==0:
                print("error at line",count,"the short word is in",word_str)
                continue
            try:
                index=ord(word[0])-97
            except:
                print("error at line",count,"the short word is in",word_str)
            if index<0 or index>25:
                print("error at line",count,"the unrecognized word is",word)
                continue
            for keyword in keywords[index]:
                if keyword==word:
                    if_exist=True
                    break
            if not if_exist:
                keywords[index].append(word)
        str=f.readline()
        count+=1
    f.close()
    content=""
    sum=0
    for keyword_list in keywords:
        sum+=len(keyword_list)
        result=",".join(i for i in keyword_list) 
        content+=result+"\n"
    file_new = open(filepath_new, "w")
    file_new.write(content)
    file_new.close()
    print(sum)

#replace synomys words
def syns_process(filename,file_new):
    keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    content=""
    # read old file
    file_old = open(filename,"r")
    str=file_old.readline()
    count=1
    while str!="":
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        for b in range(len(word_list)):
            syns = wordnet.synsets(word_list[b])
            # print(syns[0].name())
            syns_list=[]
            if_exist=False
            for i in range (0,len(syns)):
                for j in range (0,len(syns[i].lemmas())):
                    word_temp=syns[i].lemmas()[j].name()
                    if len(word_temp)==0:
                        print("the short word is in",word_temp)
                        continue
                    try:
                        index=ord(word_temp[0])-97
                    except:
                        print("the short word is in",word_temp)
                    if index<0 or index>25:
                        # print("the unrecognized word is",word_temp)
                        continue
                    for a in range(0,len(keywords[index])):
                        if keywords[index][a]==word_temp:
                            word_list[b]=word_temp
                            # print("changed from", word_list[b],"to",word_temp)
                            if_exist=True
                            break
                    if if_exist:
                        break
                if if_exist:
                    break
            if not if_exist:
                if len(word_list[b])==0:
                    # print("the short word is in",word_list[b])
                    continue
                try:
                    index=ord(word_list[b][0])-97
                except:
                    print("the short word is in",word_list[b])
                    continue
                if index<0 or index>25:
                    # print("the unrecognized word is",word_list[b])
                    continue
                keywords[index].append(word_list[b]) 
        line_splited[len(line_splited)-2]=" ".join(i for i in word_list)
        if line_splited[len(line_splited)-1]!="\n":
            line_splited[len(line_splited)-1]="\n"
        result="	".join(i for i in line_splited)
        content+=result
        str=file_old.readline()
        count+=1
        # print(count)
    file_old.close()
    #  write new file
    file_new = open(file_new, "w")
    file_new.write(content)
    file_new.close()
    print("Synomys process done")
#store keywords that have high frequency
def get_frequent_keyword(filepath,filepath_new):
    f=open(filepath,"r")
    str=f.readline()
    count=1
    # list of word sort by first character
    keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    keywords_count=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    while str!="":
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        for word in word_list:
            if_exist=False
            if len(word)==0:
                print("error at line",count,"the short word is in",word_str)
                continue
            try:
                index=ord(word[0])-97
            except:
                print("error at line",count,"the short word is in",word_str)
            if index<0 or index>25:
                print("error at line",count,"the unrecognized word is",word)
                continue

            for i in range(0,len(keywords[index])):
                if keywords[index][i]==word:
                    keywords_count[index][i]+=1
                    if_exist=True
                    break
            if not if_exist:
                keywords[index].append(word)
                keywords_count[index].append(1)
        str=f.readline()
        count+=1
    f.close()
    sum_frequent=0
    sum=0
    frequent_keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range (0,26):
        for j in range(0,len(keywords[i])):
            sum+=1
            # the words shows up lease than 10 times will be droped, if the occurance of the word is too high, we count it as common word and drop it too
            if keywords_count[i][j]<=9999 and keywords_count[i][j]>=10:
                # print(keywords[i][j])
                sum_frequent+=1
                frequent_keywords[i].append(keywords[i][j])
    content=""
    for keyword_list in frequent_keywords:
        result=",".join(i for i in keyword_list) 
        content+=result+"\n"
    file_new = open(filepath_new, "w")
    file_new.write(content)
    file_new.close()
    print("Get frequent key process done")
    # print(sum)
    # print(sum_frequent)
    
def getCombinedData(company,start,oldfile,newfile):
    ones=[]
    zeros=[]
    stock_prediction=get_stock_price(company,start)
    file_old = open(oldfile,"r")
    str=file_old.readline()
    while str!="":   
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        date=line_splited[1][0:10]   
        d=date_difference(start,date)+1
        if d==0:
            continue
        temp=[]
        count0=0
        count1=0
        print(stock_prediction[d][0],date)
        for a in range (0,7): 
            if stock_prediction[d+a][2]==1:
                count1+=1
            elif stock_prediction[d+a][2]==0:
                count0+=1
        if count1>count0:
            ones.append(word_str)
        else:
            zeros.append(word_str)
        str=file_old.readline()
    content=""
    content+="= = = zero = = =\n"
    for sentence in zeros:
        content+=sentence+"\n"
    content+="= = = one = = =\n"
    for sentence in ones:
        content+=sentence+"\n"
    file_new = open(newfile, "w")
    file_new.write(content)
    file_new.close()

def getimdb(company,start,oldfile,newfile):
    ones=[]
    zeros=[]
    stock_prediction=get_stock_price(company,start)
    file_old = open(oldfile,"r")
    str=file_old.readline()
    while str!="":   
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        date=line_splited[1][0:10]   
        d=date_difference(start,date)+1
        if d==0:
            continue
        temp=[]
        count0=0
        count1=0
        print(stock_prediction[d][0],date)
        for a in range (0,7): 
            if stock_prediction[d+a][2]==1:
                count1+=1
            elif stock_prediction[d+a][2]==0:
                count0+=1
        if count1>count0:
            ones.append(word_str)
        else:
            zeros.append(word_str)
        str=file_old.readline()
    content=""
    for sentence in ones:
        content+="pos\t"+sentence+"\n"
    for sentence in zeros:
        content+="neg\t"+sentence+"\n"
    
    file_new = open(newfile, "w")
    file_new.write(content)
    file_new.close()
              
        
if __name__ == '__main__':
    # process_original_data("2020_12_08To2021_04_03.txt","PFE_new.txt") #this will omit all Bullish and Bearish words
    # get_file_dictionary("PFE_new.txt","PFE_keyword_dict.txt") #this will genarate all keyword (it is not have to run)
    get_frequent_keyword("test2.txt","PFE_frequent.txt") #this will genarate frequent keywords 
    # syns_process("PFE_new.txt")