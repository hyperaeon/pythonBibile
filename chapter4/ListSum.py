__author__ = 'hzliyong'

def ListSum(L) :
    result = 0
    for i in L:
        result = result + i
    return result

L = [1, 2, 3, 4]
print(ListSum(L))

def Cube(x = None, y = 2, z = 3) :
    return ( x + y - z) ** 3

print(Cube(x = 3, z = 5))

def mylistappend(*list) :
    l = []
    for i in list:
        l.extend(i)
    return l

a = [1 , 2 , 4]
b = (3 , 5, 7)
print(mylistappend(a, b ))

def changeValue(x):
    x[0] = x[0] ** 2

b = [2]
changeValue(b)
print(b)

def fun(x):
    global a
    return a + x
a = 5
print(fun(3))

fun = lambda x : x * x - x
print(fun(3))

def show():
    print('lambda')
f = lambda:show()
f()
