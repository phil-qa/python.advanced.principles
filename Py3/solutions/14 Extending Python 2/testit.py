#!/usr/local/bin/python3
import sys
import MkDict

print("Test1 - create a dictionary")
keys   = ['Australia', 'Eire', 'France', 'Finland', 'UK', 'US']
values = ['Canberra', 'Dublin', 'Paris', 'Helsinki', 'London', 'Washington']
countries = MkDict.MkDict(keys = keys, values = values)

print(countries)
print("Ref count:", sys.getrefcount(countries)) 

print("\nTest 2 - assign None for missing values")
keys   = ['Ford', 'Honda', 'Renault', 'Ferrari', 'Bentley']
values = ['Focus', 'CRV', 'Espace']
cars = MkDict.MkDict(keys, values)
print(cars)

print("\nTest 3 - ignore extra values")
keys   = ['M42', 'C33', 'M8', 'M17']
values = ['Orion', 'Veil', 'Lagoon', 'Swan', 'Dumbell', 'Crab']
nebula = MkDict.MkDict(values = values, keys = keys)
print(nebula)

for key in nebula.keys():
    print("Ref count:", sys.getrefcount(key)) 
