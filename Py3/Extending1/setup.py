#!/usr/local/bin/python3

from distutils.core import setup, Extension

module1 = Extension('MkDict',
                    sources = ['MkDict.c'])

setup (name = 'MkDict',
       version = '1.0',
       description = 'Create a dictionary from two lists',
       ext_modules = [module1])
