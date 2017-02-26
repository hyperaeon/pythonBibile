# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import tkinter
import threading
import socket

class ListenThread(threading.Thread):
    def __init__(self, edit, server):
        threading.Thread.__init__(self)
        self.edit = edit
        self.server = server

    def run(self):
        while 1:
            try:
                client, addr = self.server.accept()
                self.edit.insert(tkinter.END,
                                 '连接来自：%s:%d \n' % addr)
                data = client.recv(1024)
                self.edit.insert(tkinter.END,
                                '收到数据：%s \n' % data)
                client.send(str('I GOT: %s' % data).encode())
                client.close()
                self.edit.insert(tkinter.END,
                                 '关闭客户端\n')
            except:
                self.edit.insert(tkinter.END,
                                 '关闭连接\n')
                break

class Control(threading.Thread):
    def __init__(self, edit):
        threading.Thread.__init__(self)
        self.edit = edit
        self.event = threading.Event()
        self.event.clear()


    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', 1051))
        server.listen(1)
        self.edit.insert(tkinter.END,
                                 '正在等待连接\n')
        self.lt = ListenThread(self.edit, server)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        server.close()


    def stop(self):
        self.event.set()


class Window:
    def __init__(self, root):
        self.root = root
        self.butlisten = tkinter.Button(root,
                                        text = '开始监听', command = self.Listen)
        self.butlisten.place(x = 20, y = 15)
        self.butclose = tkinter.Button(root,
                                        text = '停止监听', command = self.Close)
        self.butclose.place(x = 120, y = 15)
        self.edit = tkinter.Text(root)
        self.edit.place(y = 50)

    def Listen(self):
        self.ctrl = Control(self.edit)
        self.ctrl.setDaemon(True)
        self.ctrl.start()

    def Close(self):
        self.ctrl.stop()

root = tkinter.Tk()
window = Window(root)
root.mainloop()


