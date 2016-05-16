#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='poyo',
    version='0.3.0',
    author='Raphael Pierzina',
    author_email='raphael@hackebrot.de',
    maintainer='Raphael Pierzina',
    maintainer_email='raphael@hackebrot.de',
    license='MIT',
    url='https://github.com/hackebrot/poyo',
    description='A lightweight YAML Parser for Python',
    long_description=read('README.rst'),
    packages=[
        'poyo',
    ],
    package_dir={'poyo': 'poyo'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
    keywords=['YAML', 'parser'],
)
