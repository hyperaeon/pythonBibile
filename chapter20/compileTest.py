__author__ = 'hzliyong'

import re

r  = re.compile('go*d')
r.match('Life can be good')
r.match('Life can be good', 12)

r = re.compile('b.\sg')
r.search('Life can be good')

r = re.compile('\w.\sg')
r.search('Life can be good')

r = re.compile('\\b\w..?\s')
print(r.findall('Life can be good'))

s = '''Life can be good;
    Life can be bad;
    Life is mostly cheerful;
    But sometimes sad.'''
r = re.compile('b\w*', re.I)
new = r.sub('*', s)
print(new)

new = r.sub('*', s, 2)
print(new)

r = re.compile('b\w*')
new = r.subn('*', s)
print(new[0])
print(new[1])



