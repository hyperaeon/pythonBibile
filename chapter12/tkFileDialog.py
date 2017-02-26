# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import tkinter.filedialog

def FileOpen():
    r = tkinter.filedialog.askopenfilename(title = 'Python tkinter', filetypes = [('Python', '*.py *.pyw'), ('All files', '*')])
    print(r)


def FileSave():
    r = tkinter.filedialog.asksaveasfilename(title = 'Python tkinter', initialdir = r'D:\Developer\Python', initialfile = 'test.py')
    print(r)


root = tkinter.Tk()
button1 = tkinter.Button(root, text = 'FileOpen', command = FileOpen)
button1.pack(side = 'left')
button2 = tkinter.Button(root, text = 'FileSave', command = FileSave)
button2.pack(side = 'left')
root.mainloop()

def a(x):
    def b(y):
        return x + y
    return b
print(a(2))
print(a(2)(3))

