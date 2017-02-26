# coding:utf-8

__author__ = 'hzliyong'

import tkinter
import tkinter.messagebox
import os, os.path
import threading
import tkinter.simpledialog
import scanBigFile

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
        menu.add_cascade(label = "搜索", menu = submenu)

        self.root.config(menu = menu)

        #创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root, anchor = tkinter.W, text = '状态', bitmap = 'hourglass', compound = 'left')
        self.progress.place(x = 10, y = 370, width = 480, height = 15)

        #创建文本框，显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x = 10, y = 10, width = 480, height = 350)

        #为文本框添加垂直动态
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side = 'right', fill = 'y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title('PyOptimize')
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    #“关于”菜单
    def MenuAbout(self):
        tkinter.messagebox.showinfo("PyOptimize", "这是使用python编写的Windows优化程序。\n欢迎使用并提出宝贵意见！")

    #“退出”菜单
    def MenuExit(self):
        self.root.quit()

    #“扫描垃圾文件”菜单
    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("PyOptimize", "扫描垃圾文件将需要较长的时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("PyOptimize", "马上开始扫描垃圾文件")
        #self.ScanRubbish()
        self.drives = self.GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    #删除垃圾文件
    def DeleteRubbish(self, scanpath):
        global rubbishExt
        total = 0
        fileSize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
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

    #“扫描垃圾文件”
    def ScanRubbish(self, scanpath):
        global rubbishExt
        self.flist.delete(0.0, tkinter.END)
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)#根据'.'分割文件名和扩展名
                        if filesplit[1] == '':#没有扩展名
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:#扩展名在垃圾文件扩展名列表中
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


    #“删除垃圾文件”菜单
    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("PyOptimize", "删除垃圾文件将需要较长的时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("PyOptimize", "马上开始删除垃圾文件！")
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
        s = tkinter.simpledialog.askinteger('PyOptimize', '请设置大文件的大小(M)')
        t = threading.Thread(target=self.ScanBigFile, args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion("PyOptimize", "扫描大文件将需要较长的时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("PyOptimize", "马上开始扫描大文件！")

    #搜索大文件
    def ScanBigFile(self, fileSize):
        fSize = fileSize * 1024 * 1024#转化成B
        s = scanBigFile(fSize)
        total = scanGi
        # for drive in self.GetDrives():
        #     for root, dirs, files in os.walk(drive):
        #         for file in files:
        #             try:
        #                 fname = os.path.join(os.path.abspath(root), file)
        #                 singleSize = os.path.getsize(fname)
        #
        #                 self.progress['text'] = fname
        #                 if singleSize > fSize:
        #                    total += 1
        #                    self.flist.insert(tkinter.END, '%s, [%.2f M] \n' % (fname, singleSize / 1024/ 1024))
        #             except:
        #                 pass
        self.progress['text'] = "找到%s个超过%sM的大文件" % (total, fSize/ 1024/1024)



    #“按名称搜索文件”菜单
    def MenuSearchFile(self):
        s = tkinter.simpledialog.askstring('PyOptimize', "请输入文件名的部分字符")
        t = threading.Thread(target=self.SearchFile, args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion("PyOptimize", "按名称搜索文件将需要较长的时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("PyOptimize", "马上开始按名称搜索文件！")

    #按名称搜索文件
    def SearchFile(self, fname):
        total = 0
        fname = fname.upper()
        for drive in self.GetDrives():
            for root, dirs, files in os.walk(drive):
                for file in files:
                    try:
                        fn = os.path.join(os.path.abspath(root), file)
                        l = len(fn)
                        if l > 50:
                            self.progress['text'] = fn[:25] + "..."  + fn[l-25:]
                        else:
                            self.progress['text'] = fn
                        if file.upper().find(fname) > 0:#包含fname的文件
                            total += 1
                            self.flist.insert(tkinter.END, fn + '\n')
                    except:
                        pass
        self.progress['text'] = "找到%s个文件" % (total)


if __name__ == "__main__":
    window = Window()
    window.MainLoop()
