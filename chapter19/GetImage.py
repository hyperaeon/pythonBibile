# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.gifs = []
        self.jpgs = []

    def handle_starttag(self, tags, attrs):
        if tags == 'img':
            for attr in attrs:
                for t in attr:
                    if 'png' in t:
                        self.gifs.append(t)
                    elif 'jpg' in t:
                        self.jpgs.append(t)
                    else:
                        pass

    def get_gifs(self):
        return self.gifs

    def get_jpgs(self):
        return self.jpgs

class Window:
    def __init__(self, root):
        self.root = root
        self.label = tkinter.Label(root, text = '输入URL：')
        self.label.place(x = 5, y = 15)
        self.entryUrl = tkinter.Entry(root, width = 30)
        self.entryUrl.place(x = 65, y = 15)
        self.get = tkinter.Button(root, text = '获取图片', command = self.Get)
        self.get.place(x = 280, y = 15)
        self.edit = tkinter.Text(root, width = 470, height = 600)
        self.edit.place(y = 50)

    def Get(self):
        url = self.entryUrl.get()
        page = urllib.request.urlopen(url)
        data = page.read()
        parser = MyHTMLParser()
        parser.feed(data.decode())
        self.edit.insert(tkinter.END, '====GIF====\n')
        gifs = parser.get_gifs()
        for gif in gifs:
            self.edit.insert(tkinter.END, gif + '\n')
        self.edit.insert(tkinter.END, '===========\n')
        self.edit.insert(tkinter.END, '====JPG====\n')
        jpgs = parser.get_jpgs()
        for jpg in jpgs:
            self.edit.insert(tkinter.END, jpg + '\n')
        self.edit.insert(tkinter.END, '=========\n')
        page.close()

root = tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()
