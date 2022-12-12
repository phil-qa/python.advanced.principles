#!/usr/local/bin/python3

from distutils.core import setup, Extension

module1 = Extension('MkList',
                    sources = ['MkList.c'])

setup (name = 'MkList',
       version = '1.0',
       description = 'Create a list from a dictionary',
       ext_modules = [module1])
