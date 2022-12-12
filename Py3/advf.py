#!/usr/local/bin/python3
# advf.py Python 3

import sys
import inspect

# TODO: insert your decorator here

# line_no = inspect.getouterframes(inspect.currentframe())[1][2]

def myfunc1(): pass


def myfunc2(): pass


def myfunc3(p = 0):
    """ Multiply arg by 2 """
    print(p * 2)

myfunc1()
myfunc2()
myfunc3(42)
myfunc1()

print(myfunc1.__name__)
help(myfunc3)
     