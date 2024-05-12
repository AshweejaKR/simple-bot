# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:47:55 2024

@author: ashwe
"""

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "simple-bot",
    version = "0.0.0",
    author = "ashwe",
    author_email = "",
    description = (""),
    long_description = read('README.md'),
)

