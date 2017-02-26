# -*- coding:utf-8 -*-


__author__ = 'hzliyong'

list = []
list.append(1)
list.count(2)
list.extend([2, 3, 4, 5])
list.index(5)

dic = {'apple' : 2, 'orange' : 1}
print(dic.copy())
dic['banana'] = 5
print(dic['banana'])
print(dic.items())
print(dic.pop('apple'))
print(dic)
print(dic.pop('apple', 3))
print(dic.update({'apple': 2}))
dic.clear()
print(dic)