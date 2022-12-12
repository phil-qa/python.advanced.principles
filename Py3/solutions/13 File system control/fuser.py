#!/usr/local/bin/python3
import psutil
import sys
import os.path

if len(sys.argv) < 2:
    exit("Please supply a file name")

target = sys.argv[1]
print(target+":\t",end="")

if sys.platform == 'win32':
    target = target.lower().replace('/','\\')   

if os.path.isdir(target):
    isdir = True
else:
    isdir = False

for proc in psutil.process_iter():
    try:
        flist = proc.open_files()
        if flist:
            for nt in flist:
                if sys.platform == 'win32':
                    name = nt.path.lower()
                else:
                    name = nt.path
                
                if name == target:
                    print(proc.pid,end=" ")
            
        if sys.platform == 'win32':
            cwd = proc.getcwd().lower()
        else:
            cwd = proc.getcwd()
            
        if isdir and target == cwd:
            print(proc.pid,end="c ")
        
    except psutil.AccessDenied:
        pass
    except psutil.NoSuchProcess:
        pass
       
print() 
