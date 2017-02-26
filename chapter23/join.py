__author__ = 'hzliyong'

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        x = 0
        time.sleep(60)
        print(self.id)

def func():
    t.start()
    t.join()
    for i in range(5):
        print(i)
t = MyThread(2)
func()