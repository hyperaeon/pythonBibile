__author__ = 'hzliyong'

import pdb


class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

try:
    raise MyError('Raise MyError')
except MyError as data:
    print(data)
else:
    print('No error')

pdb.set_trace()
for i in range(0, 5):
    i = i * 5
    print(i)