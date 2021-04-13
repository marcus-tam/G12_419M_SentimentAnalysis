from nltk.corpus import wordnet

def syns_test(word):
    syns = wordnet.synsets(word)
    # print(syns[0].name())
    syns_list=[]
    for i in range (0,len(syns)):
        for j in range (0,len(syns[i].lemmas())):
            syns_list.append(syns[i].lemmas()[j].name())
    syns_list.sort()
    print(syns_list[0])

if __name__=='__main__':
    syns = wordnet.synsets("./")
    syns_list=[]
    for i in range (0,len(syns)):
        for j in range (0,len(syns[i].lemmas())):
            syns_list.append(syns[i].lemmas()[j].name())
    for word in syns_list:
        syns_test(word)
    
