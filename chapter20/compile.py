__author__ = 'hzliyong'

import re
s = 'Python can run on Windows'
print(re.findall('\\bo.+?\\b', s))
print(re.findall('\\Bo.+?', s))
print(re.findall('\so.+?', s))
print(re.findall('\\b\w.+?\\b', s))
print(re.findall('\d\.\d', 'Python 2.5'))
print(re.findall('\D+', 'Python 2.5'))
print(re.split('\s', s))
print(re.split("\s", s, 1))
print(re.findall('\d\w+?', 'abc3de'))