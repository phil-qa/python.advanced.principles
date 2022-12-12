#!/usr/local/bin/python3
"""
    From Pi.cpp    Ed Strassberger            2007-08-22
 
    Try various algorithms for calculating Pi
 
     3.14159265358979323846264
"""
from Pi_arctan import pi_arctan
from Pi_triangle import pi_triangle


if __name__ == "__main__":
    
    num_steps = 21000000
    nThreads = 1
    dx = 1. / num_steps

    option = 'm'            # show menu first time and on demand

    while True:

        if option == 'm':

            print("\n\n\t\t\tPi Menu   Rev 1.0\n\n",
                  "  m = show menu\n\n",
                  "  n = Set iterations, currently", num_steps, " dx is", dx, "\n\n",
                  "  t = Set threads, currently", nThreads, "\n\n",
                  "  1 = arctan: sum(y*dx) where y = 4/(1 + x*x) for x = 0...1 by dx\n\n",
                  "  2 = triangle: 4*sum(y*dx) where y = sqrt(1 - x*x) for x = 0...1 by dx\n\n",
                  "  q = quit\n")

        option = input("Enter selection: ")

        if option == 'n':
            num_steps = int(input("\nEnter iterations: "))

            dx = 1. / num_steps
            print("\nnum_steps is now", num_steps, ", making its reciprical dx =", dx)
            break

        elif option == 't':
            nThreads = int(input("\nEnter number of threads(%d): " % (nThreads)))

        elif option == '1':
            print("\nComputing Pi by the arctan method...")
            pi = pi_arctan(num_steps, dx, nThreads)
            print(pi)

        elif option == '2':
            print("\nComputing Pi by the triangle method...")
            pi = pi_triangle(num_steps, dx, nThreads);
            print(pi)

        elif option == 'q':
            break
