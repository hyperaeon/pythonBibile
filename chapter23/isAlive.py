__author__ = 'hzliyong'

import threading
import time

class mythread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        time.sleep(5)
        print(self.id)

t = mythread(1)
def func():
    t.start()
    print(t.isAlive())
func()