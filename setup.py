#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages

with open('README.html') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'colorama>=0.3.9'
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(jawahar273): put setup requirements
    # (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='pntl',
    version='0.2.3.2',
    description=("used to interface with Senna and"
                 " stanford-parser.jar for dependency parsing"),
    long_description='\n\n' + readme + '\n\n' + history,
    author='Jawahar S',
    author_email='jawahar273@gmail.com',
    url='https://github.com/jawahar273/practNLPTools-lite',
    packages=find_packages(include=['pntl']),
    entry_points={
        'console_scripts': [
            'pntl=pntl.cli:user_test'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='practnlptools-lite senna python pntl pysenna'.split(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
