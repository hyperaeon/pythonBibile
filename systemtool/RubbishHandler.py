# coding:utf-8

__author__ = 'hzliyong'

import os
import tkinter

class rubbish:
    def __init__(self, scanpath, rubbishExt, progress, flist):
        self.scanpath = scanpath
        self.rubbishExt = rubbishExt
        self.progress = progress
        self.flist = flist

    #“扫描垃圾文件”
    def scanRubbish(self):
        total = 0
        filesize = 0
        for drive in self.scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)#根据'.'分割文件名和扩展名
                        if filesplit[1] == '':#没有扩展名
                            continue
                        try:
                            if self.rubbishExt.index(filesplit[1]) >= 0:#扩展名在垃圾文件扩展名列表中
                                fname = os.path.join(os.path.abspath(root), fil)
                                sigleSize = os.path.getsize(fname)
                                filesize += sigleSize
                                # if total % 20 == 0:
                                #     self.flist.delete(0.0, tkinter.END)
                                fileMSize = sigleSize/1024
                                self.flist.insert(tkinter.END, fname + " " + str(fileMSize) + 'K\n')
                                l = len(fname)
                                if l > 40:
                                    fullname = fname[:30] + "..." + fname[l-30:]
                                    self.progress['text'] = fullname
                                else:
                                    self.progress['text'] = fname
                                total += 1#计数
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "找到%s个垃圾文件，共占用%.2f M磁盘空间" % (total, filesize/1024/1024)

    #删除垃圾文件
    def deleteRubbish(self):
        total = 0
        fileSize = 0
        for drive in self.scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if self.rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(os.path.abspath(root), fil)
                                fileSize += os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    if l > 50:
                                        fname = fname[:25] + "..." + fname[l-25:]
                                        if total % 15 == 0:
                                            self.flist.delete(0.0, tkinter.END)
                                        self.flist.insert(tkinter.END, 'Deleted ' + fname + '\n')
                                        self.progress['text'] = fname
                                        total += 1
                                except:
                                    pass
                        except ValueError as e:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "删除%s个垃圾文件，收回%.2fM磁盘空间" % (total, fileSize / 1024/ 1024)