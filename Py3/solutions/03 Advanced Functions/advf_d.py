#!/usr/local/bin/python3
# advf.py Part 3 Python 2

import sys
import inspect
from functools import wraps, partial

def logger(func=None, stream=None):
    
    if func is None:
        return partial(logger, stream=stream)
        
    if stream is None:
        stream = sys.stderr
        
    @wraps(func)
    def wrapper(*args, **kwargs):
        line_no = inspect.getouterframes(inspect.currentframe())[1][2]
        mesg = "%s called from line %d" % \
                    (func.__name__, line_no) 
        print (mesg, file=stream)
        return func(*args, **kwargs)
            
    return wrapper
    
@logger
def myfunc1(): pass

fo = open('log.txt', 'w')
@logger(stream=fo)
def myfunc2(): pass


@logger
def myfunc3(p = 0):
    """ Multiply arg by 2 """
    print(p * 2)

myfunc1()
myfunc2()
myfunc3(42)
myfunc1()

fo.close()

print(myfunc1.__name__)
help(myfunc3)