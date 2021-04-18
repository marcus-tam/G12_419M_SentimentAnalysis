
import numpy
def bag_of_words(filepath_data,filepath_keywords):
    frequent_keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    keywords_vector=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    keywords_vectors=[]
    file_keywords = open(filepath_keywords,"r")   
    for i in range (0,26) :
        str=file_keywords.readline()
        if(str==""):
            continue
        keywords_list=str.split(",")
        for keyword in keywords_list:
            frequent_keywords[i].append(keyword)
            keywords_vector[i].append(0)
    file_keywords.close()
    indent=0
    if filepath_data=="trainAAPL_new.txt":
        indent=5
    elif filepath_data=="trainAMZN_new.txt" or filepath_data=="trainPFE_new.txt":
        indent=2
    
    file_data = open(filepath_data,"r")  
    str=file_data.readline()
    count=1
    while str!="":
        ifdelete=True
        keywords_vector_temp=[]
        for i in range (0,26):
            keywords_vector_temp.append(numpy.zeros(len(keywords_vector[i])))      
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        for word in word_list:
            if len(word)==0:
                # print("word is",word)
                continue
            index=ord(word[0])-97
            if index<0 or index>25:
                # print(word,index)
                continue
            for i in range(0,len(frequent_keywords[index])):
                if frequent_keywords[index][i]==word:
                    ifdelete=False
                    keywords_vector_temp[index][i]+=1
                    break
        if ifdelete:
            # print(count)
            str=file_data.readline()
            count+=1
            continue
        temp=[]
        for vector in keywords_vector_temp:
            for value in vector:
                temp.append(value)
                # result=",".join(i+"" for i in temp)      
        temp.append(line_splited[1][0:10])
        keywords_vectors.append(temp)
        
        # print(temp)
        str=file_data.readline()
        count+=1
        if indent!=0:
            for i in range(0,indent):
                str=file_data.readline()
        # if count>=10000:
        #     break
    file_data.close()

    # numpy.savetxt('new_test2.csv', keywords_vectors, delimiter = ',')
    # print(keywords_vectors)
    return keywords_vectors

def convertToID(filepath_data,filepath_keywords):
    frequent_keywords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    keywords_vectors=[]
    file_keywords = open(filepath_keywords,"r")   
    for i in range (0,26) :
        str=file_keywords.readline()
        if(str==""):
            continue
        keywords_list=str.split(",")
        for keyword in keywords_list:
            frequent_keywords[i].append(keyword)
    file_keywords.close()
    start=numpy.zeros(26)
    start[0]=0
    for i in range(1,26):
        start[i]=start[i-1]+len(frequent_keywords[i-1])
    file_data = open(filepath_data,"r")  
    str=file_data.readline()
    length=0
    lengths=[]
    while str!="":
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        lengths.append(len(word_list))
        if len(word_list)>length:
            length=len(word_list)
        str=file_data.readline()
    file_data.close()

    file_data = open(filepath_data,"r")  
    str=file_data.readline()

    while str!="":
        ifdelete=True
        keywords_vector_temp=[]
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")     
        current_index=0 
        for word in word_list:
            if len(word)==0:
                continue
            index=ord(word[0])-97
            if index<0 or index>25:
                continue
            for i in range(0,len(frequent_keywords[index])):
                if frequent_keywords[index][i]==word:
                    ifdelete=False
                    id=start[index]+i
                    keywords_vector_temp.append(id)
                    current_index+=1
                    break
        if ifdelete:
            str=file_data.readline()
            continue  
        # for a in range(current_index,length):
        #       keywords_vector_temp.append(0)
        keywords_vector_temp.append(line_splited[1][0:10])
        keywords_vectors.append(keywords_vector_temp)
        str=file_data.readline()
    file_data.close()
    # print(keywords_vectors)
    # print(set(lengths))
    return keywords_vectors

if __name__=='__main__':
    keywords_vectors=convertToID("trainMCD_new.txt","MCD_frequent.txt")
    print(len(keywords_vectors))
    

    