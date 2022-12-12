#!/usr/local/bin/python3

from distutils.core import setup, Extension

module1 = Extension('Tidy',
                    sources = ['Tidy.c','Win32Specifics.c'])

setup (name = 'TidyPackage',
       version = '1.0',
       description = 'Delete .o files and chmod .sh files',
       ext_modules = [module1])
