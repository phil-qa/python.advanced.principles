#!/usr/local/bin/python3
import os
print("PID:",str(os.getpid()))
while True:
    
    input("press <RETURN> to open file");
    fh = open("/tmp/test.txt",'w')

    print("Opened /tmp/test.txt...");
    input("press <RETURN> to close");

    fh.close()
