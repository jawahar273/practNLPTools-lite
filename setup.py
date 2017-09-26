#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
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
    version='0.2.0',
    description="used to interface with Senna and stanford-parser.jar",
    long_description=readme + '\n\n' + history,
    author="Jawahar S",
    author_email='jawahar273@gmail.com',
    url='https://github.com/jawahar273/practNLPTools-lite',
    packages=find_packages(include=['pntl']),
    entry_points={
        'console_scripts': [
            'pntl=pntl.cli:test'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='practNLPTools-lite senna python pntl pysenna',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
