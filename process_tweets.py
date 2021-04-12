
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

    file_data = open(filepath_data,"r")  
    str=file_data.readline()
    count=1
    while str!="":
        keywords_vector_temp=[]
        for i in range (0,26):
            keywords_vector_temp.append(numpy.zeros(len(keywords_vector[i])))      
        line_splited=str.split("	")
        word_str=line_splited[len(line_splited)-2]
        word_list=word_str.split(" ")
        for word in word_list:
            if len(word)==0:
                print("word is",word)
                continue
            index=ord(word[0])-97
            if index<0 or index>25:
                print(word,index)
                continue
            for i in range(0,len(frequent_keywords[index])):
                if frequent_keywords[index][i]==word:
                    keywords_vector_temp[index][i]+=1
                    break
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
        if count==40:
            break
    file_data.close()

    # numpy.savetxt('new_test2.csv', keywords_vectors, delimiter = ',')
    # print(keywords_vectors)
    return keywords_vectors

if __name__=='__main__':
    keywords_vectors=bag_of_words("PFE_new.txt","PFE_frequent.txt")
    

    