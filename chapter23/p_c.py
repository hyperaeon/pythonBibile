# -*- coding:utf-8 -*-
import threading
__author__ = 'hzliyong'


global num


class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        global x
        con.acquire()
        if x == num:
            con.wait()
            pass
        else:
            for i in range(num):
                x = x + 1
            con.notify()
        print(x)
        con.release()


class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            con.wait()
            pass
        else:
            for i in range(num):
                x = x - 1
            con.notify()
        print(x)
        con.release()


num = 100000
con = threading.Condition()
x = 0
p = Producer('Producer')
c = Consumer("Consumer")
p.start()
c.start()
p.join()
c.join()
print(x)