#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Python 3

books = {"1234":{'title':"New Ideas",
                 'author':"Fred Smith",
                 'price':u"\xA3" "19.99"},
                 
         "2345":{'title':"Bad Ideas",
                 'author':"Joe Bloggs",
                 'price':u"\xA3" "9.99"}
         }

import codecs
import json
fo = open('books.json','w')
json.dump(books, fo, ensure_ascii=False)
fo.close()

import yaml
fo = open('books.yaml', 'w')
yaml.dump(books, fo)
fo.close()

import pickle
fo = open('books.pky', 'wb')
pickle.dump(books, fo)
fo.close()

from xml.etree.ElementTree import Element, tostring
def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
    
e = dict_to_xml('books', books)

print(tostring(e))


