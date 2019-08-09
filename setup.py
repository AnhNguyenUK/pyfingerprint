#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pyfingerprint',
    version='1.5',
    install_requires=['pyserial', 'pillow'],
    description='Python written library for using ZhianTec fingerprint sensors.',
    author='Bastian Raschke',
    author_email='bastian.raschke@posteo.de',
    url='https://sicherheitskritisch.de',
    license='D-FSL',
    packages=['pyfingerprint'],
    package_dir={'': 'src'},
    zip_safe=False,
)
