#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages
from json import load

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.rst") as history_file:
    history = history_file.read()


setup_requirements = [
    "pytest-runner",
    # TODO(jawahar273): put setup requirements
    # (distutils extensions, etc.) here
]

# read the `extras_require.json` for getting
# extras_require depencencys.
extras_require = load(open("extras_require.json"))


def parse_requirements(filename):
    """ load requirements from a pip requirements file
        refer: `link <https://stackoverflow.com/questions/25192794/no-module-named-pip-req/>`_
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name="pntl",
    version="0.3.0",
    description=(
        "used to interface with Senna and" " stanford-parser.jar for dependency parsing"
    ),
    long_description="\n\n" + readme + "\n\n" + history,
    author="Jawahar S",
    author_email="jawahar273@gmail.com",
    url="https://github.com/jawahar273/practNLPTools-lite",
    packages=find_packages(include=["pntl.*"]),
    entry_points={"console_scripts": ["pntl=pntl.cli:user_test"]},
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    license="MIT license",
    zip_safe=False,
    keywords="practnlptools-lite senna python pntl pysenna".split(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    test_suite="tests",
    tests_require=parse_requirements("requirements_dev.txt"),
    setup_requires=setup_requirements,
    extras_require=extras_require,
)
