# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import angular-chess
version = angular-chess.__version__

setup(
    name='angular-chess',
    version=version,
    author='',
    author_email='will@django.nu',
    packages=[
        'angular-chess',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['angular-chess/manage.py'],
)