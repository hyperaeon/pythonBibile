# coding:utf-8

__author__ = 'hzliyong'

import math
import tkinter
import tkinter.messagebox
import os, os.path
import threading
import tkinter.simpledialog
from Search import search
from RubbishHandler import *

rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk', '._mp', '.gid', '.chk', '.syd', '.$$$', '.@@@', '.~*']

class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        #创建菜单
        menu = tkinter.Menu(self.root)

        #创建“系统”子菜单
        submenu = tkinter.Menu(menu, tearoff = 0)
        submenu.add_command(label = "关于...", command = self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label = "退出", command = self.MenuExit)
        menu.add_cascade(label = "系统", menu = submenu)

        #创建“清理”子菜单
        submenu = tkinter.Menu(menu, tearoff = 0)
        submenu.add_command(label = "扫描垃圾文件", command = self.MenuScanRubbish)
        submenu.add_command(label = "删除垃圾文件", command = self.MenuDelRubbish)
        menu.add_cascade(label = "清理", menu = submenu)

        #创建“查找”子菜单
        submenu = tkinter.Menu(menu, tearoff = 0)
        submenu.add_command(label = "搜索大文件", command = self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label = "按名称搜索文件", command = self.MenuSearchFile)
        submenu.add_command(label = "按扩展名搜索文件", command = None)
        menu.add_cascade(label = "搜索", menu = submenu)

        self.root.config(menu = menu)

        #创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root, anchor = tkinter.W, text = '状态', bitmap = 'hourglass', compound = 'left')#bitmap的值有"error"，"hourglass"，"info"，"question"，"warning"
        self.progress.place(x = 10, y = 370, width = 480, height = 20)

        #创建文本框，显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x = 10, y = 10, width = 480, height = 350)

        #为文本框添加垂直动态
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side = 'right', fill = 'y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title('Windows系统工具')
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    #“关于”菜单
    def MenuAbout(self):
        tkinter.messagebox.showinfo("Windows系统工具", "这是使用python编写的Windows优化程序。\n欢迎使用并提出宝贵意见！")

    #“退出”菜单
    def MenuExit(self):
        self.root.quit()

    #“扫描垃圾文件”菜单
    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("Windows系统工具", "扫描垃圾文件将需要较长的时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Windows系统工具", "马上开始扫描垃圾文件")
        #self.ScanRubbish()
        self.drives = self.GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    #删除垃圾文件
    def DeleteRubbish(self, scanpath):
        global rubbishExt
        self.flist.delete(0.0, tkinter.END)
        s = rubbish(scanpath, rubbishExt, self.progress, self.flist)
        s.deleteRubbish()

    #“扫描垃圾文件”
    def ScanRubbish(self, scanpath):
        global rubbishExt
        self.flist.delete(0.0, tkinter.END)
        s = rubbish(scanpath, rubbishExt, self.progress, self.flist)
        s.scanRubbish()


    #“删除垃圾文件”菜单
    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("Windows系统工具", "删除垃圾文件将需要较长的时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Windows系统工具", "马上开始删除垃圾文件！")
        self.drives = self.GetDrives()
        # t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))
        # t.start()

    #取得当前计算机的盘符
    def GetDrives(self):
        drives = []
        for i in range(65, 90):
            vol = chr(i) + ":\\"
            if os.path.isdir((vol)):
                drives.append(vol)
        return tuple(drives)

    #“搜索大文件”菜单
    def MenuScanBigFile(self):
        s = tkinter.simpledialog.askinteger('Windows系统工具', '请设置大文件的大小(M)')
        t = threading.Thread(target=self.ScanBigFile, args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion("PyOptimize", "扫描大文件将需要较长的时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("PyOptimize", "马上开始扫描大文件！")

    #搜索大文件
    def ScanBigFile(self, fileSize):
        self.flist.delete(0.0, tkinter.END)
        if fileSize is None:
            return
        fSize = fileSize * 1024 * 1024#转化成字节
        s = search(fSize, self.GetDrives(), self.progress, self.flist)
        total = s.scanFile()
        self.progress['text'] = "找到%s个超过%sM的大文件" % (total, fSize/ 1024/1024)



    #“按名称搜索文件”菜单
    def MenuSearchFile(self):
        self.flist.delete(0.0, tkinter.END)
        s = tkinter.simpledialog.askstring('Windows系统工具', "请输入文件名的部分字符")
        t = threading.Thread(target=self.SearchFile, args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion("PyOptimize", "按名称搜索文件将需要较长的时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("PyOptimize", "马上开始按名称搜索文件！")

    #按名称搜索文件
    def SearchFile(self, fname):
        total = 0
        if fname is None:
            return
        s = search(None, self.GetDrives(), self.progress, self.flist)
        total = s.searchFile(fname.upper())

if __name__ == "__main__":
    window = Window()
    window.MainLoop()
