#!/usr/local/bin/python3
import psutil
import sys
import os.path

if len(sys.argv) < 2:
    exit("Please supply a file name")

target = sys.argv[1]
print(target+":\t",end="")

if os.path.isdir(target):
    isdir = True
else:
    isdir = False

for proc in psutil.process_iter():
    try:
        flist = proc.open_files()
        if flist:
            for nt in flist:
                if nt.path == target:
                    print(proc.pid,end=" ")

        if isdir and target == proc.getcwd():
            print(proc.pid,end="c ")
     
    except psutil.AccessDenied:
        pass
    except psutil.NoSuchProcess:
        pass
       
print() 
