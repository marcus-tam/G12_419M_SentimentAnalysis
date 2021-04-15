def filemod(filename):
    f = open(filename, 'r')
    w = open("train_testReddit/"+filename, 'w')
    for line in f.readlines():
        w.write(line[:-1] + "\t" + line[-1:])
    f.close()
    w.close()


def pol(filename):
    f = open(filename, 'r')
    temp = f.readline()
    temp = (temp[:7] + temp[(8):])
    print(temp)
    return temp

def pog(filename):
    f = open(filename, 'r')
    temp = (f.readline())
    print(temp)
    return temp

# pol = pol('trainRedditAAPL.txt')
# pog = pog('trainRedditAAPL.txt')

# if(pol == pog):
#     print("true")

filenames = {'testRedditAAPL.txt', 'testRedditBRK.B.txt', 'testRedditMCD.txt', 'testRedditPFE.txt', 'trainRedditAAPL.txt', 'trainRedditBRK.B.txt', 'trainRedditMCD.txt', 'trainRedditPFE.txt'}
for filename in filenames:
    filemod(filename)