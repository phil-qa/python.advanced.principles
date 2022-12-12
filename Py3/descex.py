#!/usr/local/bin/python3
# Python 3 delegate version

class CheckType(object):
   # Implement your descriptor class here
   pass
   
   
   
# CheckType tests
import datetime
class Person(object):
    pname = CheckType("pname", str)
    pdob  = CheckType("pdob", datetime.date)
    pstat = CheckType("pstat", int)

# The following should not produce errors    
p1 = Person()
p1.pname = "Fred Bloggs"
p1.pdob = datetime.date(1956, 1, 31)
print(p1.pname)

# The following should raise warnings
import warnings
try:
    del(p1.pname)
except AttributeError as err:
    warnings.warn(err)
    
try:
    p1.pname = 42
except TypeError as err:
    warnings.warn(err)
    
try:
    p1.pdob = "Fred Bloggs"
except TypeError as err:
    warnings.warn(err)
    
try:
    p1.pstat = Person 
except TypeError as err:
    warnings.warn(err)
