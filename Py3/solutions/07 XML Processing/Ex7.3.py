#!/usr/local/bin/python3
# Ex7.3.py  Python 3 version
# A script to load an XML document as a DOM and then add new elements.

import datetime

import xml.dom.minidom     
doc = xml.dom.minidom.parse('books.xml')

# Define a function to add a publication date node to a given node.
# Additional text nodes may be needed for formatting purposes.
def add_pub(node):
    tabs = doc.createTextNode('\n\t\t')
    pub = doc.createElement('PubDate')
    val = doc.createTextNode(datetime.date.today().strftime("%d/%m/%Y"))

    pub.appendChild(val)
    node.insertBefore(tabs, node.lastChild)
    node.insertBefore(pub, node.lastChild)

# Get the book entries and add a the PubDate element
for book in doc.getElementsByTagName('book'):
    add_pub(book)

# Save the new XML
out = open('newbooks.xml', 'w')
doc.writexml( out )         # Save it
out.close()

print(doc.toxml())          # Display it on stdout

