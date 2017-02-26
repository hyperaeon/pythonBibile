# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import tkinter.simpledialog


def InStr():
    r = tkinter.simpledialog.askstring('Python tkinter', 'Input String', initialvalue = 'tkinter')
    print(r)


def InInt():
    r = tkinter.simpledialog.askinteger('Python tkinter', 'Input Integer')
    print(r)


def InFlo():
    r = tkinter.simpledialog.askfloat('Python tkinter', 'Input Float')
    print(r)

root = tkinter.Tk()
button1 = tkinter.Button(root, text = 'Input String', command = InStr)
button1.pack(side = 'left')
button2 = tkinter.Button(root, text = 'Input Integer', command = InInt)
button2.pack(side = 'left')
button3 = tkinter.Button(root, text = 'Input Float', command = InFlo)
button3.pack(side = 'left')
root.mainloop()