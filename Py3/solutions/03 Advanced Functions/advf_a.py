#!/usr/local/bin/python3
# advf.py Part (a) Python 3

import sys
import inspect

def logger(func):
    line_no = inspect.getouterframes(inspect.currentframe())[1][2]
    mesg = "%s called from line %d" % \
           (func.__name__, line_no) 
    print(mesg)
    
    return func
    
@logger
def myfunc1(): pass

@logger
def myfunc2(): pass

@logger
def myfunc3(p = 0):
    """ Multiply arg by 2 """
    print(p * 2)

myfunc1()
myfunc2()
myfunc3(42)
myfunc1()

print(myfunc1.__name__)
help(myfunc3)
     