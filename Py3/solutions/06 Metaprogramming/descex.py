#!/usr/local/bin/python3
# Python 3 version
class CheckType(object):
   
    def __init__(self, aname, atype):
        self.aname = "_" + aname
        self.type = atype
  
    def __get__(self, inst, cls):
        return getattr(inst, self.aname, self.type)
        
    def __set__(self, inst, value):
        if isinstance(value, self.type):
            setattr(inst, self.aname, value)
        else:
            raise TypeError("Incorrect type, was %s requires %s" % (type(value), self.type))
        
    def __delete__(self, inst):
        raise AttributeError("You may not delete attribue %s" % (self.aname))

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
