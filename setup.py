#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import jose

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


setup(
    name='python-jose',
    version=jose.__version__,
    author='Michael Davis',
    author_email='mike.philip.davis@gmail.com',
    description='JOSE implementation in Python',
    license='MIT',
    keywords='jose jws jwe jwt json web token security signing',
    url='http://github.com/mpdavis/jose',
    packages=get_packages('jose'),
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    install_requires=[
        'pycrypto==2.6.1',
        'six==1.9.0',
    ]
)
