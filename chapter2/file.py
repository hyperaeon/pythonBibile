__author__ = 'hzliyong'

import math


file = open(r'e:\test.txt', 'w')
file.write('python\n')

a = []
for i in range(10):
    s = str(i) + '\n'
    a.append(s)

file.writelines(a)
file.close()

file = open(r'e:\test.txt', 'r')
s = file.read()
print(s)

m = 'hi'
n = 'hello'
if m == n:
    print('true')
elif m > n:
    print('false')
else :
    print(m, n)

for i in [1, 2, 3, 4, 5, 6]:
    if i == 6 :
        break
    if i == 2:
        continue
    print(i)
else:
    print('all')

people = {'tom' : 170, 'Jack' : 175, 'Kite' : 160}
for name in people:
    print(people[name])

tt = (('a', 'b'), ('c', 'd'), ('e', 'f'))
for t1 in tt:
    print(t1)

for (x, y) in tt:
    print(x, y)

for i in range(50, 100 + 1):
    for t in range(2 , int(math.sqrt(i)) + 1):
        if i % t == 0:
            break
    else :
        print(i)