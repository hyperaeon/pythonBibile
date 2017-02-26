# coding:utf-8

__author__ = 'hzliyong'

import os, os.path

def traverse(pathname):
    for item in os.listdir(pathname):
        fullitem = os.path.join(pathname, item)
        print(fullitem)
        if os.path.isdir(fullitem):
            traverse(fullitem)

traverse("E:\桌面")
str = 'abcdefg'
print(str[3:1])
print(str[3:-1])