# coding:utf-8

import os,os.path,re

__author__ = 'hzliyong'

def Map(sourceFile, targetFile):
    sFile = open(sourceFile, 'r')
    dataLine = sFile.readline()
    tempData = {}

    if not os.path.isdir(targetFile):
        os.mkdir(targetFile)

    while dataLine:
        p_re = re.compile(r'(GET|POST)\s(.*?)\sHTTP/1.[01]', re.IGNORECASE)

        match = p_re.findall(dataLine)
        if match:
            visitUrl = match[0][1]
            if visitUrl in tempData:
                tempData[visitUrl] += 1
            else :
                tempData[visitUrl] = 1
        dataLine = sFile.readline()
    sFile.close()

    tList = []
    for key, value in sorted(tempData.items(), key = lambda k : k[1], reverse = True):
        tList.append(key + " " + str(value) + '\n')

    tFileName = os.path.join(targetFile, os.path.split(sourceFile)[1] + "_map.txt")
    tFile = open(tFileName, 'a+')
    tFile.writelines(tList)
    tFile.close()

if __name__ == "__main__":
    Map("access\\access.txt1.txt", "access")
    Map("access\\access.txt2.txt", "access")
    Map("access\\access.txt3.txt", "access")
    Map("access\\access.txt4.txt", "access")
