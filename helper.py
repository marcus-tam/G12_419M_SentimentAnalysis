from numpy import exp
import time
import datetime
def date_difference(date1,date2):
    date1=time.strptime(date1,"%Y-%m-%d")
    date2=time.strptime(date2,"%Y-%m-%d")
    date1=datetime.datetime(date1[0],date1[1],date1[2])
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    d=date2-date1
    return d.days

if __name__=='__main__':
    print(date_difference("2020-11-08","2020-12-09"))