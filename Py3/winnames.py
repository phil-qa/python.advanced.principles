#!/usr/local/bin/python3
from ctypes import *
from ctypes.wintypes import *

MAX_PATH = 260 + 1

def GetShortName(LongName):
    kernel = windll.kernel32
    
    pBuff = create_unicode_buffer(MAX_PATH)

    retn = kernel.GetShortPathNameW(LongName,pBuff,MAX_PATH)
    
    if retn == 0:
        raise WindowsError(WinError())
    
    return wstring_at(pBuff)

def GetLongName(ShortName):
    kernel = windll.kernel32
    
    pBuff = create_unicode_buffer(MAX_PATH)

    retn = kernel.GetLongPathNameW(ShortName,pBuff,MAX_PATH)
    
    if retn == 0:
        raise WindowsError(WinError())
    
    return wstring_at(pBuff)

if __name__ == '__main__':
    shorty = GetShortName("C:\\Program Files")
    print("Short name:",shorty)
    longy  = GetLongName (shorty)
    print("Long name :",longy)
