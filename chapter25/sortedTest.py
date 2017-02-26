__author__ = 'hzliyong'

dic = {"a": 1, "b": 2, "c": 3}

for key, value in sorted(dic.items(), key = lambda k : k[1], reverse = True):
    print(key + " " +str(value))