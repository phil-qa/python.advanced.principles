#!/usr/local/bin/python3
"""
// pi_arctan.cpp        Ed Strassberger        2007-08-22
//
//    Compute Pi by the arctan formula (Is that correct??)
"""
import mytimer
from threading import Thread
from queue import Queue

def pi_arctan(num_steps, dx, nThreads):

    sum = 0.0

    def doit(spos, epos, resultq):

        lsum = 0
        for i in range(spos, epos):
            x = (i + 0.5) * dx
            lsum += 1.0 / (1. + x*x)

        resultq.put(lsum)


    threads=[]
    mytimer.start_timer()
    resultq = Queue()
    
    steps_per_thread = int(num_steps/nThreads) + 1
    
    for thread in range(0, nThreads):
        spos = (steps_per_thread * thread) + 1
        epos = spos + steps_per_thread
        if epos > num_steps: epos = num_steps
         
        th = Thread(target=doit, args=(spos, epos, resultq))
        print("Processing %d to %d" % (spos, epos))
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()
        sum += resultq.get()
                 
    mytimer.end_timer('Thread')  

    pi = 4 * sum * dx

    return pi

