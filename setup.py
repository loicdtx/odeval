#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from setuptools import setup, find_packages
import os

# Parse the version from the main __init__.py
with open('odeval/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


setup(name='odeval',
      version=version,
      description=u"object detection evaluation",
      author=u"Rafael Padilla, Loic Dutrieux",
      author_email='loic.dutrieux@cirad.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy',
                        'matplotlib'],
      # scripts=[],
     )
