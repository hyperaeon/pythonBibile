# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import tkinter.messagebox

class MyDialog:
    def __init__(self, root):
        self.top = tkinter.Toplevel(root)
        label = tkinter.Label(self.top, text = 'Please Input')
        label.pack()
        self.entry = tkinter.Entry(self.top)
        self.entry.pack()
        self.entry.focus()
        button = tkinter.Button(self.top, text = 'Ok', command = self.Ok)
        button.pack()

    def Ok(self):
        self.input = self.entry.get()
        self.top.destroy()

    def get(self):
        return self.input

class MyButton():
    def __init__(self, root, type):
        self.root = root
        if type == 1:
            self.button = tkinter.Button(root, text = 'Create', command = self.Create)
            self.button.pack()
        else :
            self.button = tkinter.Button(root, text = 'Quit', command = self.Quit)
            self.button.pack()


    def Create(self):
        d = MyDialog(self.root)
        self.button.wait_window(d.top)
        tkinter.messagebox.showinfo('Python', 'Your input:\n' + d.get())

    def Quit(self):
        self.root.quit()

root = tkinter.Tk()
MyButton(root, 0)
MyButton(root, 1)
root.mainloop()