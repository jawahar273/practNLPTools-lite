#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pntl` package."""
from os import getcwd
from os.path import join, split as path_split

import pytest

from click.testing import CliRunner

from pntl import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    pass


# def test_command_line_interface():
#     """Test the CLI."""
#     def get_senna_path(*value):

#         temp = path_split(getcwd())[0]

#         return join(temp, *value)

#     runner = CliRunner()
#     result = runner.invoke(cli.user_test, ["-SE", get_senna_path("pntl", "senna", "")])
#     # assert result.exit_code == 0
#     assert "pntl.cli.user_test" in result.output
