# -*- coding:utf-8 -*-

__author__ = 'hzliyong'

import re
import sys

def DealWithFunc(s):
    r = re.compile(r'''
        (?<=def\s)
        \w+
        \(.*?\)
        (?=:)
        ''', re.X | re.U)
    return r.findall(s)

def DealWithVar(s):
    vars = []
    r = re.compile(r'''
        \b
        \w+
        (?=\s=)
        ''', re.X | re.U)
    vars.extend(r.findall(s))
    r = re.compile(r'''
        (?<=for\s)
        \w+
        \s
        (?=in)
        ''', re.X | re.U)
    vars.extend(r.findall(s))
    return vars

if len(sys.argv) == 1:
    source = input('请输入要处理的文件路径')
else:
    source = sys.argv[1]
file = open(source, encoding = 'utf-8')
s = file.readlines()
file.close()
print('*********************************')
print(source, '中的函数有：')
print('*********************************')
i = 0
for line in s:
    i = i + 1
    function = DealWithFunc(line)
    if len(function) == 1:
        print('Line:', i, '\t', function[0])

print('*********************************')
print(source, '中的函数有：')
print('*********************************')
for line in s:
    i = i + 1
    var = DealWithVar(line)
    if len(var) == 1:
        print('Line:', i, '\t', var[0])
