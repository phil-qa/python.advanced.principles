#!/usr/local/bin/python3
"""
   pi_triangle.cpp      Ed Strassberger     2007-08-22
  
    Compute Pi by the triangle (Pythagorean Theorem) formula
  
    Pi is 4 times the area of one quadrant of a unit circle
  
    The quadrant of the circle is composed of num_steps slices, each
    dx = 1 / num_steps wide.
    Each trapezoid height y is the height of the right triangle
    formed by the hypotenuse (radius = 1) of the circle and the base x.
    y = sqrt(1 - x*x) and the area of the strip is y * dx.
  
    |
    |     /||
    |  1 / ||
    |   /  ||
    |  /   ||
    | /    ||
    |/     ||
    0______||_________1______
           x
"""
import math
import mytimer
from threading import Thread
from queue import Queue

def pi_triangle(num_steps, dx, nThreads):

    sum = 0.0
      
    def doit(spos, epos, resultq):
    
       lsum = 0
       for i in range(spos, epos):
           x = (i + 0.5) * dx            # trapezoidal rule takes middle of dx
           lsum += math.sqrt(1. - x*x) * dx     # Pythagorean theorem gives y, dx gives area
    
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

    pi = 4 * sum     # only integrated 1/4 of circle

    return pi

