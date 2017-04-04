# coding:utf-8

__author__ = 'hzliyong'

import math
import tkinter
import tkinter.messagebox
import os, os.path
import threading
import tkinter.simpledialog
import FileSplilt

from tkinter import filedialog
from Search import search
from RubbishHandler import *


rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk', '._mp', '.gid', '.chk', '.syd', '.$$$', '.@@@', '.~*']
fileTypes =  [('log', '*.log'), ('text','.txt'), ('Python', '*.py *.pyw'), ('All files', '*.*')]

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
        menu.add_cascade(label = "文件清理", menu = submenu)

        #创建“查找”子菜单
        submenu = tkinter.Menu(menu, tearoff = 0)
        submenu.add_command(label = "搜索大文件", command = self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label = "按名称搜索文件", command = self.MenuSearchFile)
        submenu.add_command(label = "按扩展名搜索文件", command = None)
        menu.add_cascade(label = "文件搜索", menu = submenu)

        #创建“文件分割”子菜单
        # submenu = tkinter.Menu(menu, tearoff = 0)
        # submenu.add_command(label = "分割大文件", command = self.MenuSplitFile)
        # menu.add_cascade(label = "文件分割", menu = submenu)


        self.root.config(menu = menu)

        '''
        分割文件相关的配置
        '''
        self.sourceLabel = tkinter.Label(self.root, text = '请选择要分割的文件:')
        self.sourceLabel.place(x = 10, y = 10, width = 140, height = 20)
        self.sourceTxt = tkinter.Text(self.root)
        self.sourceTxt.place(x = 140, y = 10, width = 300, height = 20)
        self.sourceButton = tkinter.Button(self.root, text = "浏览", command = self.fileOpen1)
        self.sourceButton.place(x = 450, y = 10, width = 40, height = 25)

        self.destLabel = tkinter.Label(self.root, text = '被分割文件目标文件夹:')
        self.destLabel.place(x = 10, y = 40, width = 140, height = 20)
        self.destTxt = tkinter.Text(self.root)
        self.destTxt.place(x = 140, y = 40, width = 300, height = 20)

        self.tipLabel = tkinter.Label(self.root, text = '请输入每个文件的行数:')
        self.tipLabel.place(x = 10, y = 70, width = 140, height = 20)
        self.tipTxt = tkinter.Text(self.root)
        self.tipTxt.place(x = 140, y = 70, width = 300, height = 20)
        self.splitButton = tkinter.Button(self.root, text = "分割", command = self.MenuSplitFile)
        self.splitButton.place(x = 450, y = 70, width = 40, height = 25)

        #创建文本框，显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x = 10, y = 110, width = 480, height = 350)

        #为文本框添加垂直动态
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side = 'right', fill = 'y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

        #创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root, anchor = tkinter.W, text = '状态', bitmap = 'hourglass', compound = 'left')#bitmap的值有"error"，"hourglass"，"info"，"question"，"warning"
        self.progress.place(x = 10, y = 470, width = 480, height = 20)

    def MainLoop(self):
        self.root.title('Windows系统工具')
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.mainloop()

    #打开文件命令
    def fileOpen1(self):
        r = filedialog.askopenfilename(title = '选择需要分割的文件', filetypes = fileTypes)
        self.sourceTxt.delete(0.0, tkinter.END)
        self.sourceTxt.insert(tkinter.END, r)

    #打开文件命令
    def fileOpen2(self):
        r = filedialog.askopenfilename(title = '选择被分割文件的目标文件夹', filetypes = fileTypes)
        self.destTxt.delete(0.0, tkinter.END)
        self.destTxt.insert(tkinter.END, r)

    #“关于”菜单
    def MenuAbout(self):
        tkinter.messagebox.showinfo("Windows系统工具", "这是使用python编写的Windows优化程序。主要包含以下功能：\n"
                                                   "1、系统\n"
                                                   "2、文件清理\n"
                                                   "3、文件搜索\n"
                                                   "4、文件分割")

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
        self.flist.delete(0.0, tkinter.END)#tkinter.END表示结尾，.delete(0.0, tkinter.END)表示从开始到结尾的内容全部删掉
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

    #“按文件名称分割文件”菜单
    def MenuSplitFile(self):
        self.flist.delete(0.0, tkinter.END)
        t = threading.Thread(target= self.SplitFile, args = (self.sourceTxt.get(0.0, tkinter.END), self.destTxt.get(0.0, tkinter.END), self.tipTxt.get(0.0, tkinter.END)))
        t.start()

    #分割文件的具体实现逻辑
    def SplitFile(self, source, dest, tip):
        self.flist.delete(0.0, tkinter.END)
        source = source.strip()
        dest = dest.strip()
        tip = tip.strip()
        if source == "":
            tkinter.messagebox.showerror("错误提示", "请选择需要分割的文件")
            return
        if dest == '':
            tkinter.messagebox.showerror("错误提示", "请输入被分割文件的目标文件夹")
            return
        if tip == '':
            tkinter.messagebox.showerror("错误提示", "请输入每个文件的行数")
            return
        try:
            int(tip)
        except:
            tkinter.messagebox.showerror("错误提示", "文件行数必须是整数")
            return
        FileSplilt.split(source, dest, int(tip), self.flist, self.progress)



if __name__ == "__main__":
    window = Window()
    window.MainLoop()
