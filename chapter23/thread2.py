__author__ = 'hzliyong'


import threading

def run(x, y):
    for i in range(x, y):
        print(i)

t1 = threading.Thread(target = run, args = (15, 20))
t1.start()

t2 = threading.Thread(target = run, args = (7, 11))
t2.start()
