__author__ = 'hzliyong'

class Booook:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''

    def show(self):
        print(self.__author)
        print(self.__name)

    def setname(self, name):
        self.__name = name

a = Booook()
a.show()
a.setname('linken')
a.show()
