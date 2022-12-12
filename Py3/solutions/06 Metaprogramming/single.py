#!/usr/local/bin/python3
# Python 3 version
# Implement your Singleton metaclass here

class Singleton(type):
   
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)        
  
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        
        return self.__instance

class TheBoss(metaclass = Singleton):
       
    def __init__(self, name):
        self.__name = str(name)

    def __str__(self):
        return self.__name

p1 = TheBoss("Fred")
print(p1)
p2 = TheBoss("Jim")
print(p2)

del(p1)
del(p2)
p3 = TheBoss(None)
print(p3)
p4 = TheBoss("Harry")
print(p4)