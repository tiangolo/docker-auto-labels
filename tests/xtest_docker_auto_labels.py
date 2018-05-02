#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `docker_auto_labels` package."""


import unittest
from click.testing import CliRunner

from docker_auto_labels import cli


class TestDocker_auto_labels(unittest.TestCase):
    """Tests for `docker_auto_labels` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def xtest_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'docker_auto_labels.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
