__author__ = 'hzliyong'


class Book:
    author = ''
    name = ''
    pages = 0
    price = 0
    press = ''


Book.author = 'Jack'
a = Book()
print(a)
print(a.author)
a.author = 'tom'
print(a.author)
Book.author = 'Jack'
print(a.author)
print(a.author)
b = Book()
print(b.author)

class A:
    name = 'A'
    num = 2

print(A.name)

a = A()
print(a.name)
b = A()
print(b.name)

a.name = 'C'
A.name = 'B'
print(a.name)
print(b.name)
