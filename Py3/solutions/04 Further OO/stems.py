#!/usr/local/bin/python3
# Python 3 version
import mytimer

with mytimer.Mytimer("Load") as t:
    stems = {}

    for row in open ("words"):
        for count in range(1, len(row)):
            stem = row[0:count]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1
            #print("stem:",stem,"value:<",stems[stem],">")    

# Process the stems

with mytimer.Mytimer("Stem timer") as t:
    n = 30
    
    for stem_size in range(2, n+1):
        best_stem = ""
        best_count = 0

        for stem, count in stems.items():
            if stem_size == len(stem) and count > best_count:
               best_stem  = stem
               best_count = count

        if best_stem:
            print("Most popular stem of size", stem_size, "is:",
                   best_stem, "(occurs", best_count, "times)")
                



