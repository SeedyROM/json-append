#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of json-append.
# https://github.com/SeedyROM/json-append

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

import json

from .exceptions import (
        ErrorLoadingJSONFile,
        NoJSONFileSpecified
        )


class JSONReader:
    """Simple class to hold the state of a currently parsed file.
    """
    def __init__(self, file_path=None):
        """Initialize our class and set some defaults.
        """
        self.file_path = file_path
        self.current_file = None
        self.data = dict()

    def load(self, file_path=None):
        """Load a file either from state or specified file_path.
        """
        self.file_path = file_path or self.file_path

        if self.file_path is None:
            raise NoJSONFileSpecified

        try:
            with open(self.file_path, 'r+') as f:
                self.current_file = f.read()
        except BaseException:
            raise ErrorLoadingJSONFile

        self.data = json.loads(self.current_file)

    def set(self, key, value):
        """Set a value in our current data context.
        """
        self.data[key] = value

    def __setitem__(self, key, value):
        """Dictionary style interface to self.set()
        """
        self.set(key, value)

    def get(self, key):
        """Get a value from our current data context.
        """
        return self.data.get(key)

    def __getitem__(self, key):
        """Dictionary style interface to self.get()
        """
        value = self.get(key)

        if value is None:
            raise KeyError

        return value

    def write(self, file_path=None):
        self.file_path = file_path or self.file_path
        with open(self.file_path, 'w') as f:
            f.write(json.dumps(self.data))


def reader(*args, **kwargs):
    """Factory function to generate a new JSONReader
    """
    return JSONReader(*args, **kwargs)
