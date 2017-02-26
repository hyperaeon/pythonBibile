# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter

root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root,
                            variable = r,
                            value = '1',
                            indicatoron = 0,
                            text = 'Radio1')
radio.pack()

radio = tkinter.Radiobutton(root,
                            variable = r,
                            value = '2',
                            indicatoron = 0,
                            text = 'Radio2')
radio.pack()

radio = tkinter.Radiobutton(root,
                            variable = r,
                            value = '3',
                            indicatoron = 0,
                            text = 'Radio3')
radio.pack()

radio = tkinter.Radiobutton(root,
                            variable = r,
                            value = '4',
                            indicatoron = 0,
                            text = 'Radio4')
radio.pack()

c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root,
                            text = 'Checkbutton',
                            variable = c,
                            indicatoron = 0,
                            onvalue = 1,
                            offvalue = 2)
check.pack()
root.mainloop()