__author__ = 'hzliyong'


l = [1, 2, 3]
try:
    l[5]
except:
    print('Error')
else:
    print('No Error')


try:
    l[2] / 0
except IndexError:
    print('IndexError')
except ZeroDivisionError:
    print('ZeroDivisonError')
else:
    print('No Error')
finally:
    print('finally')

try:
    l[5]
except IndexError as Error:
    print(Error)
else:
    print('No Error')

try:
    raise Exception
except Exception:
    print('No Error')
else:
    print('No Error')

try:
    raise Exception('Raise an Exception')
except Exception as data:
    print(data)
else:
    print('No Error')

def fun(n):
    if n == 0:
        raise ZeroDivisionError('n is zero')
    else:
        print(n)

try:
    fun(0)
except ZeroDivisionError as data:
    print(data)
