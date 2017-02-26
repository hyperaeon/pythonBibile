__author__ = 'hzliyong'

import threading

class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        print(self.getName())


t1 = mythread('t1')
print(t1.getName())

t1.setName('T')
print(t1.getName())

t2 = mythread('t2')
t2.start()
print(t2.getName())
t2.setName('TT')
print(t2.getName())