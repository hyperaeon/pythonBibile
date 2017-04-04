# coding:utf-8

import os
import os.path
import time
import tkinter

__author__ = 'hzliyong'


def split(sourceFile, targetFolder, number, flist):
    sFile = open(sourceFile, 'r', encoding= 'utf-8')
    dataLine = sFile.readline()
    tempData = []
    fileNum = 1
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)

    while dataLine:
        for row in range(number):
            tempData.append(dataLine)
            dataLine = sFile.readline()
            if not dataLine:
                break;
        tFileName = os.path.join(targetFolder, os.path.split(sourceFile)[1] + str(fileNum) + '.txt')
        if os.path.exists(tFileName):
            os.remove(tFileName)
        tFile = open(tFileName, 'a+', encoding= 'utf-8')
        flist.insert(tkinter.END, tFileName + '\n')
        tFile.writelines(tempData)
        tFile.close()
        tempData = []
        print(tFileName + " 创建于：" + str(time.ctime()))
        fileNum += 1
    sFile.close()


if __name__ == "__main__":
    # FileSplit("access.txt", "access")
    split("dalog", "log")