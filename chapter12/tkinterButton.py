# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,
                         anchor = tkinter.E,
                         text = 'Button1',
                         width = 40,
                         height = 5)
button1.pack()
button2 = tkinter.Button(root,
                         text = 'Button2',
                         bg = 'blue')
button2.pack()
button3 = tkinter.Button(root,
                         text = 'Button3',
                         width = 14,
                         height = 1)
button3.pack()
button4 = tkinter.Button(root,
                         text = 'Button4',
                         width = 60,
                         height = 5,
                         state = tkinter.DISABLED)
button4.pack()
root.mainloop()

