__author__ = 'hzliyong'

from win32api import *
from win32con import *

def GetValues(fullname):
    name = str.split(fullname, '\\', 1)
    try:
        if name[0] == 'HKEY_LOCAL_MACHINE':
            key = RegOpenKey(HKEY_LOCAL_MACHINE, name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_CURRENT_USER':
            key = RegOpenKey(HKEY_CURRENT_USER, name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_CLASSES_ROOT':
            key = RegOpenKey(HKEY_CLASSES_ROOT, name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_CURRENT_CONFIG':
            key = RegOpenKey(HKEY_CURRENT_CONFIG, name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_USERS':
            key = RegOpenKey(HKEY_USERS, name[1], 0, KEY_READ)
        else:
            print('No key name %s' % name[0])

        info = RegQueryInfoKey(key)
        for i in range(0, info[1]):
            valueName = RegEnumValue(key, i)
            print(str.ljust(valueName[0], 20), valueName[1])
        RegCloseKey(key)
    except:
        pass

if __name__ == '__main__':
    keynames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOncEx',
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    for keyname in keynames:
        print('keyname: %s' % keyname)
        GetValues(keyname)


