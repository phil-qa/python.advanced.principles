#!/usr/local/bin/python3
# Python 3 version
import string

nato = ['zero', 'wun', 'two', 'tree', 'fower',
        'fife', 'six', 'seven', 'ait', 'niner',
        'alpha', 'bravo', 'charlie', 'delta', 'echo',
        'foxtrot', 'golf', 'hotel', 'india', 'juliet',
        'kilo', 'lima', 'mike', 'november', 'oscar', 'papa',
        'quebec', 'romeo', 'sierra', 'tango', 'uniform',
        'victor', 'whisky', 'xray', 'yankee', 'zulu']

natokeys = list(string.digits)
natokeys.extend(string.ascii_uppercase[:26])

#codes = dict(zip(natokeys, nato))
codes = {k: v for k, v in zip(natokeys, nato)}

import pprint
pprint.pprint(codes)

txt = ' '
while txt:
    txt = input("Please enter a phrase:")
    print(" ".join([codes.get(char.upper(), ' ')
                   for char in txt]))
