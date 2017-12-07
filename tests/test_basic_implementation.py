#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of json-append.
# https://github.com/SeedyROM/json-append

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

import json
import os

from preggy import expect

from json_append import parser
from json_append.exceptions import ErrorLoadingJSONFile

from tests.base import TestCase


TEST_JSON = json.dumps({
    'test1': 'testing',
})

class TestBasicImplementation(TestCase):
    def setUp(self):
        self.empty_instance = parser.reader()
        self.instance_type = self.empty_instance.__class__

        self.file_path = 'json.json'
        with open(self.file_path, 'w') as f:
            f.write(TEST_JSON)

        self.instance = parser.reader(file_path=self.file_path)
        self.instance.load()

    def tearDown(self):
        os.remove(self.file_path)

    def test_setUp_throws_no_errors(self):
        pass

    def test_parser_reader_factory_returns_valid_object(self):
        self.assertIsInstance(self.empty_instance, parser.JSONReader)

    def test_parser_reader_sets_file_path(self):
        expect(self.instance.file_path).not_error_to_happen(AttributeError)
        expect(self.instance.file_path).to_equal(self.file_path)

    def test_parser_reader_raises_error_without_file_path(self):
        try:
            self.empty_instance.load()
        except parser.NoJSONFileSpecified as e:
            assert True

    def test_parser_reader_loads(self):
        expect(self.instance.load).to_be_a_function()
        self.instance.load()

        expect(self.instance.current_file.name).to_equal(self.file_path)

    def test_parser_reader_loads_argument(self):
        argument_file_name = 'tester.json'

        with open(argument_file_name, 'w') as f:
            f.write(TEST_JSON)

        self.instance.load(argument_file_name)
        expect(self.instance.data).to_be_instance_of(dict)

        os.remove(argument_file_name)

    def test_parser_reader_loads(self):
        expect(self.instance.data).to_be_instance_of(dict)
        expect(self.instance.data.get('test1')).to_equal('testing')

    def test_parser_reader_throws_not_found(self):
        with self.assertRaises(ErrorLoadingJSONFile) as ctx:
            self.instance.file_path = 12341042392
            self.instance.load()

    def test_parser_reader_set(self):
        key, value = 'test1', 'tester123'
        self.instance.set(key, value)

        expect(self.instance.data.get(key)).to_equal(value)

    def test_parser_reader_dict_set(self):
        key, value = 'test2', 'testy321'
        self.instance[key] = value

        expect(self.instance.data[key]).to_equal(value)

    def test_parser_reader_get(self):
        expect(self.instance.get('test1')).to_equal('testing')

    def test_parser_reader_dict_get(self):
        expect(self.instance['test1']).to_equal('testing')

    def test_parser_reader_dict_get_raises_keyerror(self):
        with self.assertRaises(KeyError) as ctx:
            self.instance['321849281938912']

    def test_parser_reader_writes_changes(self):
        key, value = 'my_new_value', '12345'
        self.instance.set(key, value)
        self.instance.write()

        with open(self.file_path, 'r') as f:
            data = json.loads(f.read())

        expect(data.get(key)).to_equal(value)

    def test_parser_reader_writes_changes_to_specified_file_path(self):
        key, value = 'my_new_value', '12345'
        self.instance.set(key, value)

        file_path = 'fancy.json'
        with open(file_path, 'w') as f:
            f.write(TEST_JSON)

        self.instance.write(file_path)
        expect(self.instance.file_path).to_equal(file_path)

        with open(file_path, 'r') as f:
            data = json.loads(f.read())
        try:
            expect(data.get(key)).to_equal(value)
        finally:
            os.remove(file_path)
