#!/usr/local/bin/python3
# Ex7.1.py  Python 3 version
# Script to parse an XML file and enumerate tags

import sys
from xml.parsers import expat

# Allow user to provide a filename, or default to books.xml
filename = sys.argv[1] if sys.argv[1:] else 'books.xml'

Tags = 0
tags = {}

class ExpatError(Exception):
    pass

def start_tag(name, attr):
    global Tags, tags
    Tags += 1

    if name in tags:
        tags[name] += 1
    else:
        tags[name] = 1
    
# The following line does the same as the if/else above
# tags.get() does not raise an exception if the default value (zero here)
# is supplied.
#    tags[name] = 1 + tags.get(name, 0)

ExParser = expat.ParserCreate()
ExParser.StartElementHandler = start_tag

try:
    ExParser.ParseFile(open(filename, 'rb'))
except ExpatError:
    print("Ooops!", file=sys.stderr)
    exit(1)
else:
    for k, v in tags.items():
        print(k.ljust(15), ":", v)
    
    print("XML is well-formed and has %s tags of which %d are unique" % 
          (Tags, len(tags.keys())))


