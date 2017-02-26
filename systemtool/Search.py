# coding:utf-8

import tkinter
import tkinter.messagebox
import os

__author__ = 'hzliyong'

#扫描文件
class search:

    def __init__(self, fSize, drives, progress, flist):
        self.fSize = fSize
        self.drives = drives
        self.progress = progress
        self.flist = flist

    #搜索大文件
    def scanFile(self):
        total = 0
        for drive in self.drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    try:
                        fname = os.path.join(os.path.abspath(root), file)
                        singleSize = os.path.getsize(fname)
                        l = len(fname)
                        if l > 50:
                            self.progress['text'] = fname[:25] + "..." + fname[l-25:]
                        else:
                            self.progress['text'] = fname
                        if singleSize > self.fSize:
                           total += 1
                           self.flist.insert(tkinter.END, '%s, [%.2f M] \n' % (fname, singleSize / 1024/ 1024))
                    except:
                        pass
        return total

    #按名称搜索文件
    def searchFile(self, fname):
        total = 0
        fname = fname.upper()
        for drive in self.drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    try:
                        fn = os.path.join(os.path.abspath(root), file)
                        l = len(fn)
                        if l > 50:
                            self.progress['text'] = fn[:25] + "..." + fn[l-25:]
                        else:
                            self.progress['text'] = fn
                        if file.upper().find(fname) > 0:#包含fname的文件
                            total += 1
                            self.flist.insert(tkinter.END, fn + '\n')
                    except:
                        pass
        self.progress['text'] = "找到%s个文件" % (total)