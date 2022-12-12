#!/usr/local/bin/python3
# Py3 Delegate version
import abc
import math

class Shape(metaclass = abc.ABCMeta):
    """
     Shape abstract base class. 
    """

    """
    =====================================================================
     Place your shape functions here. The functions needed are:

     translateX()   - adjust the shape's horizontal coordinates
     translateY()   - adjust the shape's vertical coordinates
     area()         - abstract method to calculate the shape's area

    ======================================================================
    """
    
    
    
    
    """
    ======================================================================
     Prewritten shape functions
    ======================================================================
    """

    def __init__(self, x0, y0, x1, y1):
        self._left = x0
        self._top = y0
        self._right = x1
        self._bottom = y1

    def display_coords(self):
        print("Coordinates: ( %d, %d, %d, %d )" % \
             (self._left, self._top, self._right, self._bottom))

    @abc.abstractmethod
    def __del__(self):
        pass

"""
    In questions b-e, you will be asked to define derived classes
    to represent a circle, a parallelogram and a rectangle
    
    
"""

