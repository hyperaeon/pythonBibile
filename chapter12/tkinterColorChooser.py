# -*- coding:utf-8 -*-


__author__ = 'hzliyong'


import tkinter
import tkinter.colorchooser

def ChooseColor():
    r = tkinter.colorchooser.askcolor(title = 'Python tkinter')
    print(r)

root = tkinter.Tk()
button = tkinter.Button(root, text = 'Choose Color', command = ChooseColor)
button.pack()
root.mainloop()