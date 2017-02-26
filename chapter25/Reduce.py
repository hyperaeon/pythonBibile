# coding ; utf-8

import os,os.path,re

__author__ = 'hzliyong'


def Reduce(sourceFile, targetFile):
    tempData = {}
    p_re = re.compile(r'(.*?)(\d{1,}$)', re.IGNORECASE)
    for root, dirs, files in os.walk(sourceFile):
        for file in files:
            if file.endswith('_map.txt'):
                sFile = open(os.path.abspath(os.path.join(root, file)), 'r')
                # sFile = open(os.path.join(os.path.abspath(root), file), 'r')
                dataLine = sFile.readline()
                while dataLine:
                    subdata = p_re.findall(dataLine)
                    if subdata[0][0] in tempData:
                        tempData[subdata[0][0]] += int(subdata[0][1])
                    else:
                        tempData[subdata[0][0]] = int(subdata[0][1])
                    dataLine = sFile.readline()
        sFile.close()
    tList = []
    for key, value in sorted(tempData.items(), key = lambda k : k[1], reverse = True):
        tList.append(key + " " + str(value) + '\n')
    tFileName = os.path.join(sourceFile, targetFile + '_reduce.txt')
    tFile = open(tFileName, 'a+')
    tFile.writelines(tList)
    tFile.close()

if __name__ == "__main__":
    Reduce("access", "access")

