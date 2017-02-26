__author__ = 'hzliyong'

import mymodule
import sys
import os
import py_compile

print('hi')
print(mymodule.name)
print(sys.path)
modulepath = os.getcwd() + '\\module'
sys.path.append(modulepath)
print(sys.path)

py_compile.compile('mymodule.py', 'mydodule.pyc')

if __name__ == '__main__':
    print(mymodule.name)

print(dir(sys))