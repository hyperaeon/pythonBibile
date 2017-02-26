__author__ = 'hzliyong'

import os

print(os.getcwd())
path = os.getcwd()
print(os.listdir(path))
print(os.path.isdir(path))
print(os.path.isfile(path))

os.system('notepad')
# path = path + '\\temp'
# os.mkdir(path)
# os.rmdir(path)