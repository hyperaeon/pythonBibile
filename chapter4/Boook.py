__author__ = 'hzliyong'

class Boook:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''


    def __check(self, item):
        if item == '':
            return 0
        else :
            return 1

    def show(self):
        if self.__check(self.__author):
            print(self.__author)
        else:
            print('No value')
        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No value')

    def setname(self, name):
        self.__name = name


    def __init__(self, author, name):
        self.__author = author
        self.__name = name

#a = Boook('Tom', 'A wondeful book')
#a.show()


class story(Boook):
    __class = ''
    __grade = ''
    __sname = ''

    def showinfo(self):
        self.show()

s = story('Jack', 'Big book')
s.showinfo()
