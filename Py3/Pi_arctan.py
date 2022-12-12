#!/usr/local/bin/python3
"""
     pi_arctan
 
     Compute Pi by the arctan formula
"""
import mytimer

def pi_arctan(num_steps, dx, nThreads):

    sum = 0.0
    
    def doit(spos, epos):

        lsum = 0
        for i in range(spos, epos):
            x = (i + 0.5) * dx
            lsum += 1.0 / (1. + x*x)

        return lsum

    mytimer.start_timer()
    
    spos = 0
    epos = num_steps
    
    sum = doit(spos, epos)
                 
    mytimer.end_timer('Thread')  

    pi = 4 * sum * dx

    return pi

