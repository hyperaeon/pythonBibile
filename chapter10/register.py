__author__ = 'hzliyong'

import win32api
import win32con

name = 'SOFTWARE\\Python\\PythonCore\\3.5\\InstallPath'
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, name, 0, win32con.KEY_ALL_ACCESS)
print(win32api.RegQueryValue(key, ''))
win32api.RegCloseKey(key)

key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Software', 0, win32con.KEY_READ)
print(key)
win32api.RegCloseKey(key)