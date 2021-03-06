# coding:utf-8
import threading

__author__ = 'hzliyong'

class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        global event
        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName())

        else:
            print(self.getName())
            event.set()


event = threading.Event()
event.set()
tl = []
for i in range(10):
    t = mythread(str(i))
    tl.append(t)

for i in tl:
    i.start()
