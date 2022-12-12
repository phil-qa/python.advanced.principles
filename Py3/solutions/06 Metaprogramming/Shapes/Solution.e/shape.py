#!/usr/local/bin/python3
# Solution.e
import abc
import math

class Shape(metaclass = abc.ABCMeta):
    """
     Shape abstract base class. 
    """

    """
    =====================================================================
     Place your shape functions here. The functions needed are:

     translateX()       - adjust the shape's horizontal coordinates
     translateY()       - adjust the shape's vertical coordinates
     virtual area()     - calculate the shape's area

    ======================================================================
    """
    def translateX(self, offset):
        """
        adjust the shape's horizontal coordinates
        """
        self._left += offset
        self._right += offset
        
    def translateY(self, offset):
         """
         adjust the shape's vertical coordinates
         """
         self._left += offset
         self._right += offset
    
    @abc.abstractmethod
    def area(self):
        """
        calculate the shape's area
        """
        return NotImplemented    # default action
 
    @abc.abstractmethod
    def perimeter(self):
        pass
    
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
class Circle(Shape):
    
    def __init__(self, cx, cy, rad): 
        Shape.__init__(self, cx-rad, cy-rad, cx+rad, cy+rad)
    
    def area(self):    
        radius = (self._right - self._left) / 2
        return math.pi * radius * radius
    
    def perimeter(self):    
        radius = (self._right - self._left) / 2
        return 2 * math.pi * radius
    
    def __del__(self):
        print("Circle destructor")

class Parallelogram(Shape):

    def __init__(self, x0, y0, x1, y1, dx):
        Shape.__init__(self, x0, y0, x1, y1)
        self.__delta = dx
    
    def __del__(self):
        print("Parallelogram destructor")
                      
    def area(self):
        base   = abs(self._right - self._left - self.__delta)
        height = abs(self._bottom - self._top) 
    
        return base * height

    def perimeter(self):
       base   = abs(self._right - self._left - self.__delta)
       height = abs(self._bottom - self._top) 
       total = (height * height) + (self.__delta ** 2);
 
       return 2 * (math.sqrt(total)+ base)

class Rectangle(Parallelogram):

    def __init__(self, x0, y0, x1, y1):
         Parallelogram.__init__(self, x0, y0, x1, y1, 0)

    def __del__(self):
        print("Rectangle destructor")
