#!/usr/local/bin/python3
# Ex7.2.py  Python 3 version
# Using SAX to create a dictionary of book details, keyed on reference.

import xml.sax.handler

class BookHandler (xml.sax.handler.ContentHandler):
    def __init__(self):
        self.text = ''
        self.books = {}
        
    def startElement(self, name, attributes):
        global inBook
        if name == 'book':
            inBook = True
            self.ref = attributes.items()[0][1]
            
    def characters(self, data):
        if not data.isspace():
            self.text += data
            
    def endElement(self, name):
        global inBook
        if inBook:
            # Insert list separator into current text string
            self.text += ','
        if name == 'book' and inBook:
            if self.text:
                # Convert string to list
                self.books[self.ref] = self.text.rstrip(',').split(',')
                self.text = ''
            inBook = False
            
    def endDocument(self):
        for k, v in self.books.items():
            print(k, ":", v)

parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse("books.xml")

