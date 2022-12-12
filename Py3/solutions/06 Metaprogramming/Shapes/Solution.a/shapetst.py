#!/usr/local/bin/python3

"""
  Test harness to exercise the shape hierarchy

"""
from shape import *
"""
def test_b():         
    print("\nTest b")
    
    # Create derived-class object.
    # Circle constructor arguments are: (centreX, centreY, radius)

    pshape = Circle(10,10,10)       

    # The expected output is as follows:
    #   coordinates (50,100,70,120)
    #   area  314

    pshape.translateX(50)
    pshape.translateY(100)
    pshape.display_coords()

    print("Area = %d" % pshape.area())
"""

"""
def test_c():

    print("\nTest c")
    
    shptable = [ Circle(10,10,10),
                 Parallelogram(0,0,100,100,50) ]

    # The expected output is as follows:
    #   circle:         coords (10,10,30,30),   area 314
    #   parallelogram:  coords (10,10,110,110), area 5000

    for shp in shptable:
        shp.translateX(10)
        shp.translateY(10)
        shp.display_coords()

        print("Area = %d" % shp.area())

    print("\nDestroying the shapes")
"""

"""
def test_d():

    print("\nTest d")
 
    shptable = [ Circle(10,10,10),
                 Parallelogram(0,0,100,100,50),
                 Rectangle(50,50,150,150) ]

    # The expected output is as follows:
    #   circle:         coords (10,10,30,30),   area 314
    #   parallelogram:  coords (10,10,110,110), area 5000
    #   rectangle:      coords (60,60,160,160), area 10000

    for shp in shptable:
        shp.translateX(10)
        shp.translateY(10)
        shp.display_coords()
    
        print("Area = %d" % shp.area())
    
    print("\nDestroying the shapes")
"""

"""
def test_e():

    print("\nTest e")
    shptable = [ Circle(75,75,25),
                 Parallelogram(0,0,120,30,40),
                 Rectangle(200,200,300,300)]

    # The expected perimeter values are:
    #    157 for the circle
    #    260 for the parallelogram
    #    400 for the rectangle

    for shp in shptable:
        print("Perimeter = %d" % shp.perimeter())

    print("\nDestroying the shapes")
"""

if __name__ == "__main__":
    #test_b()
    #test_c()
    #test_d()
    #test_e()
    pass


