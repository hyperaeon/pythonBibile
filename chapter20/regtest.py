__author__ = 'hzliyong'

import re

s = 'Life can be good, but also can be bad'
print(re.match('can', s))
print(re.search('can', s))
print(re.match('l.*', s))
print(re.match('l.*', s, re.I))
print(re.findall('[a-z]{3}', s))
print(re.findall('[a-z]{1,3}', s))

print('------------sub------------')
s = 'Life can be bad'
print(re.sub('bad', 'good', s))
print(re.sub('bad|be', 'good', s))
print(re.sub('bad|be', 'good', s, 1))
print(re.subn('bad|be', 'good', s, 1))
r = re.subn('bad|be', 'good', s)
print(r[0])
print(r[1])

print('------------split------------')
s = 'Life can be bad'
print(re.split(' ', s))
r = re.split(' ', s, 1)
for i in r:
    print(i)

print(re.split('b', s))
