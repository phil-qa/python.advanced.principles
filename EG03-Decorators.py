import sys
import inspect

def logger(func):
    line_number = inspect.getouterframes(
        inspect.currentframe())[1][2]
    mesg = f"{func.__name__} called from {line_number}"
    print(mesg)
    return func

def adder(a,b):
    print(__name__)
    return a+b
print(adder(2,2))

@logger
def adder(a,b):
    print(__name__)
    return a+b

print(adder(4,4))

# Rewriting the logger to