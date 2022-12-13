#!/usr/local/bin/python3
import re
import sys
 
def get_value(obj, *attr):
    current_frame = sys._getframe()
    caller_frame = current_frame.f_back
    caller_frame.f_locals['in_text']
    return obj
   
def trans(in_txt):
    
    out_txt = in_txt
    for m in re.finditer(r'(#\{([^#.]*?)})|(#\{([^#]*?)\.([^.]*?)})', in_txt):
        
        pgroups = m.groups()
        if pgroups[-1] is None:
            pattern, obj = m.groups()[:2]
            value = get_value(obj)
        elif pgroups[0] is None:
            pattern, obj, attr = pgroups[2:]
            value = get_value(obj, attr)
        else:
            print("Invalid group:", pgroups)
            break
        
        out_txt = out_txt.replace(pattern, value)
        
    return out_txt

""" 
For part 3
def print(*line, sep=', ', end='\n', file=None, flush=False):
    pass
"""

# Part 1 tests
x = 42
y = 37
print(trans("x: #{x} y: #{y}"))
numbers = ['zero', 'one', 'two', 'three', 'four']
to = trans("List #{numbers}")
print(to, end = "\n\n")

# Part 2 tests
nname = 'just another [PRC].{0,6} hacker'
to = trans("Text #{nname.upper()}")
print(to)
print(trans("Platform: #{sys.platform}"), end = "\n\n")

# Part 3 tests
print("x: #{x} y: #{y}")
numbers = ['zero', 'one', 'two', 'three', 'four']
print("List #{numbers}")
print("Text #{nname.upper()}")
print("Platform: #{sys.platform}")
