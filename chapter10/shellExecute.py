__author__ = 'hzliyong'

import win32api
import win32process
from ctypes import *

win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)
win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
win32api.ShellExecute(0, 'open', 'www.baidu.com', '', '', 1)

# win32process.CreateProcess('c:\\windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())
user32 = windll.LoadLibrary('user32.dll')
user32.MessageBoxA(0, str.encode('Ctypes is cool'), str.encode('Ctypes'), 0)