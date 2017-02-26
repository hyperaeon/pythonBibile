# -*- coding:utf-8 -*-

__author__ = 'hzliyong'


import  threading
import time


class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)


    def run(self):
        global x
        # lock.acquire()
        for i in range(3):
            print("in run i=%d" % i)
            x = x + 1
        time.sleep(2)
        print(x)
        # lock.release()

lock = threading.RLock()
tl = []
for i in range(10):
    print("i=%d" % i)
    t = mythread(str(i))
    tl.append(t)
x = 0
for i in tl:
    i.start()
