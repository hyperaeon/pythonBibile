# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

from ftplib import FTP
bufsize = 1024
def Get(filename):
    command = 'RETR ' + filename
    FTP.retrbinary(command, open(filename, 'wb').write, bufsize)
    print('下载成功')

def Put(filename):
    command = 'STOR ' + filename
    filehandler = open(filename, 'rb')
    FTP.storbinary(command, filehandler, bufsize)
    filehandler.close()
    print('上传成功')

def PWD():
    print(FTP.pwd())

def Size(filename):
    print(FTP.size(filename))

def Help():
    print('''
    =======================
    Simple Python FTP
    =======================
    cd  进入文件夹
    delete  删除当前文件列表
    dir 获取当前文件列表
    get 下载文件
    help    帮助
    mkdir   创建文件夹
    put 上传文件
    pwd 获取当前目录
    rename  重命名文件
    rmdir   删除文件夹
    size    获取文件大小
    ''')


server = input('请输入FTP服务器地址：')
ftp = FTP(server)
username = input('请输入用户名：')
password = input('请输入密码：')
ftp.login(username, password)
print(ftp.getwelcome())
actions = {'dir': ftp.dir, 'pwd': PWD, 'cd': ftp.cwd, 'get':Get,
           'put':Put, 'help':Help, 'rmdir':ftp.rmd,
           'mkdir':ftp.mkd, 'delete':ftp.delete,
           'size':Size, 'rename':ftp.rename}
while True:
    print('pyftp>',)
    cmds = input()
    cmd = str.split(cmds)
    try:
        if len(cmd) == 1:
            if str.lower(cmd[0]) == 'quit':
                break
            else:
                actions[str.lower(cmd[0])]()
        elif len(cmd) == 2:
            actions[str.lower(cmd[0])](cmd[1])
        elif len(cmd) == 3:
            actions[str.lower(cmd[0])](cmd[1], cmd[2])
        else:
            print('输入错误')
    except:
        print('命令错误')
ftp.quit()
