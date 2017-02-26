__author__ = 'hzliyong'
# -*- coding:utf-8 -*-
import os
import math

a = 2
b = 3
c = a * 2 \
    + b \
    - b
print(c)

c = (a *
     b - 1
     + 3
     /
     2)
print(c)
print("你好")
# input('Input your name:')

# year = input('The year:')
# print(int(year) + 1)

l = [1, 2, 3]
t = (1, 2, 3)
print(l, t)

中国 = 'China'
print(中国)
print(2 ** 3)

print(math.cos(0.5))
print(99 ** 99)
c = 29323923929392392392939239923929392939239293
print(c)

print('%o' % (0o7 + 0o6))

m = 9 + 3j
n = 29 - 2j
print(m - n)
print(4 // 3)
print(4 / 3)

str = 'hi your O'
print(str.join('HI'))
print(str.split())
print(str.split(None, 1))
print(str.split('o', ))

print(str[0])
s = 'So %s day!'
print(s % 'beautiful')

path = r'e:\Doc'
print(os.listdir(path))