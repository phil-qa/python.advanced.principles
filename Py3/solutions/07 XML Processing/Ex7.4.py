#!/usr/local/bin/python3
# Ex7.4.py  Python 3 version
# A script to investigate the iTunes.xml file and display all tags and their
# text values.

import xml.etree.ElementTree as ET

tree = ET.parse('iTunes.xml')   
root = tree.getroot()

for book in root.iter():
    for item in book:
        print(item.tag.ljust(15), ":", item.text)
