import json
import os
import subprocess
import argparse

from preggy import expect

from json_append import cli
from tests.base import TestCase

CLI_COMMAND = ["python", "-m", "json_append.cli"]

class CLITestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = cli.arg_parser()


class TestCLIInterface(CLITestCase):
    def setUp(self):
        pass

    def test_main_runs_a_okay(self):
        with self.assertRaises(SystemExit) as ctx:
            cli.main()

    def test_cli_arg_parser_generates_an_argparse_object(self):
        self.assertIsInstance(self.parser, argparse.ArgumentParser)

    def test_cli_fails_silently_with_no_args(self):
        with self.assertRaises(SystemExit) as ctx:
            self.parser.parse_args([])

    def test_cli_accepts_valid_argument(self):
        file_path = 'testy.json'
        key, value = 'testy', 'kwargy'
        args = self.parser.parse_args([file_path, key, value])
        expect(args.file[0]).to_equal(file_path)

    def test_cli_subprocess_runs_with_no_args(self):
        result = subprocess.call(CLI_COMMAND)
        expect(result).to_be_greater_than(0)

    def test_cli_subprocess_fails_with_bad_file_path(self):
        file_path = 'testy.json'
        key, value = 'testy', 'kwargy'

        result = subprocess.call(CLI_COMMAND + [file_path, key, value])

        expect(result).to_equal(255) # -1 but it's an unsigned 8-bit int

    def test_cli_can_not_find_file(self):
        file_path = 'testy.json'
        key, value = 'testy', 'kwargy'
        args = self.parser.parse_args([file_path, key, value])
