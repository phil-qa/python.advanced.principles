#!/usr/local/bin/python3
# Part 1
import re
import sys
import builtins
 
def get_value1(obj, *attr):
    gvars = sys._getframe(1).f_globals
    lvars = sys._getframe(1).f_locals
    retn = ""
    
    if obj in lvars:
        retn = lvars[obj]
    elif obj in gvars:
        retn = gvars[obj]
    else:
        builtins.print(obj, "not found")
    
    return str(retn)
 
# Part 2
def get_value2(obj, *attr):
    gvars = sys._getframe(1).f_globals
    lvars = sys._getframe(1).f_locals
    retn = ""
    
    if obj in lvars:
        retn = lvars[obj]
        if attr:
            cmd  = obj + "." + attr[0]
            retn = eval(cmd, gvars, lvars)
            
    elif obj in gvars:
        retn = gvars[obj]
        if attr:
           cmd  = obj + "." + attr[0]
           retn = eval(cmd, gvars, lvars)
    else:
        builtins.print(obj, "not found")
    
    return str(retn)
   
def trans(in_txt):
    
    out_txt = in_txt
    for m in re.finditer(r'(#\{([^#.]*?)})|(#\{([^#]*?)\.([^.]*?)})', in_txt):
        
        pgroups = m.groups()
        if pgroups[-1] is None:
            pattern, obj = m.groups()[:2]
            value = get_value1(obj)
        elif pgroups[0] is None:
            pattern, obj, attr = pgroups[2:]
            value = get_value2(obj, attr)
        else:
            print("Invalid group:", pgroups)
            break
        
        out_txt = out_txt.replace(pattern, value)
        
    return out_txt

 
def print(*line, sep=', ', end='\n', file=None, flush=False):

    newlist = []

    for item in line:
        newlist.append(trans(str(item)))

    if file is None:
        file = sys.stdout

    builtins.print(sep.join(newlist), end=end, file=file, flush=flush)
 
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

print(x)    # This will test your string conversion
