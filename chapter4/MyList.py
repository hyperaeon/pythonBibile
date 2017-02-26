__author__ = 'hzliyong'


class MyList:
    __mylist = [ ]

    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + n

    def __sub__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - n


    def __mul__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * n

    def __div__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / n

    def __mod__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] % n

    def __pow__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] ** n

    def __len__(self):
        return len(self.__mylist)

    def show(self):
       print(self.__mylist)

l = MyList(1, 2, 3, 4, 5)
l + 5
l.show()

