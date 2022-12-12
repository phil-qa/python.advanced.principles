#!/usr/local/bin/python3
"""
This user written module contains a simple mechanism for
timing operations from Python.  It contains two functions,
start_timer(), which must be called first to initialise the
present time, and end_timer() which calculates the elapsed
CPU time and displays it.

"""
import os
start_time = 0

########################################################
# TIMER FUNCTIONS
def start_timer():
    """
    The start_timer() function marks the start of 
    a timed interval, to be completed by end_timer().
    This function requires no parameters.
    """
    global start_time
    utime, stime = os.times()[0:2]
    start_time = utime + stime

def end_timer(txt = 'End time'):
    """
    The end_timer() function completes a timed interval
    started by start_timer.  It prints an optional text
    message (default 'End time') followed by the CPU time
    used in seconds.
    This function has one optional parameter, the text to 
    be displayed.
    """
    global start_time
    if start_time == 0:
        raise SystemError(
              "end_timer() called without a start_timer()")
    utime, stime = os.times()[0:2]
    end_time = utime + stime
    print("{0:<12}: {1:01.3f} seconds".
        format(txt, end_time-start_time))
        
    start_time = 0

#######################################################
# TODO: Append Mytimer class here

class Mytimer:
    def __init__(self, txt = 'End context timer'):
        self.__txt = txt
        
    def __enter__(self):
        start_timer()
        return self
    
    def __exit__(self, *args):
        end_timer(self.__txt)
