#!/usr/local/bin/python3
# advf.py Part (c) Python 3

import sys
import inspect
from functools import wraps

def logger(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        line_no = inspect.getouterframes(inspect.currentframe())[1][2]
        mesg = "%s called from line %d" % \
                    (func.__name__, line_no) 
        print(mesg)
        return func(*args, **kwargs)
            
    return wrapper
    
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