__author__ = 'hzliyong'


class human:
    __age = 0
    __sex = ''
    __height = 0
    __weight = 0
    name = ''

    def __init__(self, age, sex, height, weight):
        self.__age = age
        self.__sex = sex
        self.__height = height
        self.__weight = weight

    def setname(self, name):
        self.name = name

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.__sex)
        print(self.__height)
        print(self.__weight)

class student(human):
    __classes = 0
    __grade = 0
    __num = 0

    def __init__(self, classes, grade, num, age, sex, height, weight):
        self.__classes = classes
        self.__grade = grade
        self.__num = num
        human.__init__(self, age, sex, height, weight)

    def show(self):
        human.show(self)
        print(self.__classes)
        print(self.__grade)
        print(self.__num)

a = student(12, 3, 20170128, 19, 'male', 180, 70)
a.setname('TOme')
a.show()