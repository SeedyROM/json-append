#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of json-append.
# https://github.com/SeedyROM/json-append

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

from setuptools import setup, find_packages
from json_append import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'coveralls',
    'sphinx',
    'pycodestyle',
    'coverage-badge'
]

setup(
    name='json-append',
    version=__version__,
    description='Append key value pairs to json files from the a cli.',
    long_description='''
Append key value pairs to json files from the a cli.
''',
    keywords='json configuration automation',
    author='Zack Kollar',
    author_email='zackkollar@gmail.com',
    url='https://github.com/SeedyROM/json-append',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'json-append=json_append.cli:main',
        ],
    },
)
