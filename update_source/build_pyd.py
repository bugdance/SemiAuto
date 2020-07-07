#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:33:20 2018

written by pyleo
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(name='any words.....',
      ext_modules=cythonize(["settings.py", "login.py", "browser.py", "order.py", "scramble.py"]))
