# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ssip209
version = ssip209.__version__

setup(
    name='ssip209_project',
    version=version,
    author='',
    author_email='max.atreides@gmail.com',
    packages=[
        'ssip209',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['ssip209/manage.py'],
)