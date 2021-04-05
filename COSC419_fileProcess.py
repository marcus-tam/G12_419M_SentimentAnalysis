
def process_original_data(filepath_old,filepath_new):
    content=""
    # read old file
    file_old = open(filepath_old,"r")
    str=file_old.readline()
    while str!="":
        line_splited=str.split("	")
        if line_splited[len(line_splited)-1]!="\n":
            line_splited[len(line_splited)-1]="\n"
        result="	".join(i for i in line_splited)
        content+=result
        str=file_old.readline()
    file_old.close()
    #  write new file
    file_new = open(filepath_new, "w")
    file_new.write(content)
    file_new.close()

def get_file_dictionary(filepath,filepath_new):
    f=open(filepath,"r")
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
            try:
                index=ord(word[0])-97
            except:
                print("error at line",count,"the short word is in",word_str)
            if index<0 or index>25:
                print("error at",count,"the unrecognized word is",word)
                continue
            for keyword in keywords[index]:
                if keyword==word:
                    break
            if not if_exist:
                keywords[index].append(word)
        str=f.readline()
        count+=1
    f.close()
    content=""
    for keyword_list in keywords:
       result=",".join(i for i in keyword_list) 
       content+=result+"\n"
    file_new = open(filepath_new, "w")
    file_new.write(content)
    file_new.close()

if __name__ == '__main__':
    # process_original_data("2020_12_08To2021_04_03.txt","PFE_new.txt")
    # get_file_dictionary("PFE_new.txt","PFE_keyword_dict.txt")