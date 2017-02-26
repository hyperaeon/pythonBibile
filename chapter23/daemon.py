# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import threading
import time

class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)

    def run(self):
        time.sleep(5)
        print(self.getName())


def func1():
    t1.start()
    print('func1 done')


def func2():
    t2.start()
    print('func2 done')

t1 = mythread('t1')
t2 = mythread('t2')
t2.daemon = True
func1()
func2()

