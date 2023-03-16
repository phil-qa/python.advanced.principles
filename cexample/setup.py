from distutils.core import setup, Extension

my_module = Extension("simple", sources=['simple.c'])

setup(
    name="simple",
    version = "0.1dev",
    description = "This is a test package",
    author = "dev guy",
    url = "https://qa.com",
    ext_modules = [my_module])