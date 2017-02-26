# coding:utf-8

__author__ = 'hzliyong'


import threading
import time
import queue

class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        global queue
        queue.put(self.getName())
        print(self.getName(), 'put ', self.getName(), ' to queue')


class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        global  queue
        print(self.getName(), 'get ', queue.get(), 'from queue')

queue = queue.Queue()
plist = []
clist = []
for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)

for i in range(10):
    c = Consumer('Consumer' + str(i))
    clist.append(c)

for i in plist:
    i.start()
    i.join()

for i in clist:
    i.start()
    i.join()
