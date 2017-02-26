__author__ = 'hzliyong'

import re
s = 'Phone No. 010-87654321'
r = re.compile(r'(\d+)-(\d+)')
m = r.search(s)
print(m)

print(m.group(1))
print(m.group(2))
print(m.group())

r = re.compile(r'(?P<Area>\d+)-(?P<No>\d+)')
m = r.search(s)
print(m.groupdict())
print(m.group('No'))
print(m.group('Area'))

s = '''Life can be good;
    Life can be bad;
    Life is mostly cheerful;
    But sometimes sad.
    '''
r = re.compile(r'be(?=\sgood)')
m = r.search(s)
print(m.span())
print(r.findall(s))
r = re.compile('be')
print(r.findall(s))

r = re.compile(r'be(?!\sgood)')
m = r.search(s)
print(m.span())
