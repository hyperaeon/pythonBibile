# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import urllib.request

str = urllib.request.quote('this is pthon')
print(str)

class Window:
    def __init__(self, root):
        self.root = root
        self.entryUrl = tkinter.Entry(root)
        self.entryUrl.place(x = 5, y = 5)
        self.get = tkinter.Button(root, text = '下载页面', command = self.Get)
        self.get.place(x = 160, y = 12)
        self.edit = tkinter.Text(root)
        self.edit.place(x = 5, y = 50)

    def Get(self):
        url = self.entryUrl.get()
        page = urllib.request.urlopen(url)
        data = page.read()
        self.edit.insert(tkinter.END, data)
        page.close()

    # def __call__(self):
    #     print('invoke __call__')


root = tkinter.Tk()
window = Window(root)
root.minsize(580, 380)
root.mainloop()
b = b'example'
print(b)

