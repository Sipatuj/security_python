import datetime
import time


f = open('mess.txt', 'a')

now_time = datetime.datetime.now()
times = now_time.strftime("%d.%m.%Y %H:%M"+'\n')

f.write(times)
#print(times)