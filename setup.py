#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='rusted',
    version='0.1.0',
    author='Messense Lv',
    author_email='messense@icloud.com',
    url='https://github.com/messense/rusted',
    keywords='rust explain error',
    description='',
    py_modules=['rusted'],
    entry_points={
        'console_scripts': [
            'rusted = rusted:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ]
)
