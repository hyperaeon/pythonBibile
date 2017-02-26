# -*- coding:utf-8 -*-

__author__ = 'hzliyong'
import poplib
import re
import tkinter

class Window:
    def __init__(self, root):
        lable1 = tkinter.Label(root, text = 'POP3')
        lable2 = tkinter.Label(root, text = 'Port')
        lable3 = tkinter.Label(root, text = '用户名')
        lable4 = tkinter.Label(root, text = '密码')
        lable1.place(x = 5, y = 5)
        lable2.place(x = 5, y = 30)
        lable3.place(x = 5, y = 55)
        lable4.place(x = 5, y = 80)
        self.entryPOP = tkinter.Entry(root)
        self.entryPort = tkinter.Entry(root)
        self.entryUser = tkinter.Entry(root)
        self.entryPass = tkinter.Entry(root, show = '*')
        self.entryPort.insert(tkinter.END, '110')
        self.entryPOP.place(x = 50, y = 5)
        self.entryPort.place(x = 50, y = 30)
        self.entryUser.place(x = 50, y = 55)
        self.entryPass.place(x = 50, y = 80)
        self.get = tkinter.Button(root, text = '收取邮件', command = self.Get)
        self.get.place(x = 60, y = 120)
        self.text = tkinter.Text(root)
        self.text.place(y = 150)

    def Get(self):
        try:
            host = self.entryPOP.get()
            port = int(self.entryPort.get())
            user = self.entryUser.get()
            pw = self.entryPass.get()
            pop = poplib.POP3(host)
            pop.user(user)
            pop.pass_(pw)
            stat = pop.stat()
            self.text.insert(tkinter.END,
                             'Status: %d message(s), %d bytes\n' % stat)
            rx_headers = re.compile(r"^(From|To|Subject)")
            for n in range(stat[0]):
                response, lines, bytes = pop.top(n + 1, 10)
                self.text.insert(tkinter.END, "Message %d (%d bytes) \n" % (n + 1, bytes))
                self.text.insert(tkinter.END, "-" * 30 + '\n')
                str_lines = []
                for l in lines:
                    str_lines.append(l.decode(encoding = 'gbk'))
                self.text.insert(tkinter.END,
                                 "\n".join(filter(rx_headers.match, str_lines)))
                self.text.insert(tkinter.END, '\n')
                self.text.insert(tkinter.END, "-" * 30 + '\n')
        except Exception as e:
            self.text.insert(tkinter.END, '接收错误\n')
            print(e)
root = tkinter.Tk()
window = Window(root)
root.mainloop()




