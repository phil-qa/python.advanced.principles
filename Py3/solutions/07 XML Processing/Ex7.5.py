#!/usr/local/bin/python3
# Ex7.5.py  Python 3 version
# A script to insert elements into an XML etree object
 
import datetime
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')    
root = tree.getroot()

# For each book, add a publication date node and additional formatting
# whitespace
for book in root.findall('book'):
    item = book[-1]
    item.tail += '\t'

    pub = ET.SubElement(book,'Published', {})
    pub.text = datetime.date.today().strftime("%d/%m/%Y") 
    pub.tail = '\n\t'

# Print out all tags and associated text
for item in root.iter():
    print(item.tag.ljust(15), ":", item.text)

tree.write('newbooks2.xml', encoding='UTF-8', xml_declaration=True)

