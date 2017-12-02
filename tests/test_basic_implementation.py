import json
import os

from preggy import expect

from json_append import parser
from tests.base import TestCase


TEST_JSON = json.dumps({
    'test1': 'testing',
    'test2': True
})

class TestBasicImplementation(TestCase):
    def setUp(self):
        self.empty_instance = parser.reader()
        self.instance_type = self.empty_instance.__class__

        self.file_path = 'json.json'
        self.instance = parser.reader(file_path=self.file_path)

        self.test_file = open(self.file_path, 'w')
        self.test_file.write(json.dumps(TEST_JSON))

    def tearDown(self):
        os.remove(self.test_file.name)

    def test_setUp_throws_no_errors(self):
        pass

    def test_parser_reader_factory_returns_valid_object(self):
        self.assertIsInstance(self.empty_instance, parser.JSONReader)

    def test_parser_reader_sets_file_path(self):
        expect(self.instance.file_path).not_error_to_happen(AttributeError)
        expect(self.instance.file_path).to_equal(self.file_path)

    def test_parser_reader_loads(self):
        expect(self.instance.load).to_be_a_function()
        self.instance.load()

        expect(self.instance.current_file).to_be_a_file()
        expect(self.instance.current_file.name).to_equal(self.file_path)

    def test_parser_reader_loads_argument(self):
        argument_file_name = 'tester.json'

        test_file = open(argument_file_name, 'w')
        test_file.write(json.dumps(TEST_JSON))

        self.instance.load(argument_file_name)

        expect(self.instance.current_file).to_be_a_file()
        expect(self.instance.current_file.name).to_equal(argument_file_name)

        os.remove(test_file.name)

        
