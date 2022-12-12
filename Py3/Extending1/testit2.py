#!/usr/local/bin/python3
import sys
import MkList

print("Test2 - create a list")
tdict   = {'Australia':'Canberra', 'Eire':'Dublin', 'France':'Paris', 
           'Finland':'Helsinki', 'UK':'London', 'US':'Washington'}

countries = MkList.MkList(tdict)
print(countries)

print("\nLoop style 1")
for i in range(len(countries)):
    print("%-12s Ref count: %d" % (countries[i], sys.getrefcount(countries[i]))) 

print("\nLoop style 2")
for val in countries:
    print("%-12s Ref count: %d" % (val, sys.getrefcount(val))) 
print("Ref counts outside:", sys.getrefcount(countries[0]), sys.getrefcount(countries[1]), "\n")

print("\nLoop style 3")
for val in MkList.MkList(tdict):
    print("%-12s Ref count: %d" % (val, sys.getrefcount(val))) 

