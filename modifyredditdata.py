def filemod(filename):
    f = open(filename, 'r')
    w = open(filename, 'w')
    for line in f.readlines():
        w.write(line[:7] + line[(8):])
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

pol = pol('trainRedditAAPL.txt')
pog = pog('trainRedditAAPL.txt')

if(pol == pog):
    print("true")