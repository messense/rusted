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
    description='Simple tool to highlight rustc --explain output',
    py_modules=['rusted'],
    install_requires=[
        'mistune>=0.7.3',
        'pygments>=2.1.3',
    ],
    entry_points={
        'console_scripts': [
            'rusted = rusted:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
    ]
)
