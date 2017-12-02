#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of json-append.
# https://github.com/SeedyROM/json-append

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

import json

class NoJSONFileSpecified(BaseException):
    pass

class JSONReader:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def load(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path

        self.current_file = open(self.file_path, 'r+')


def reader(*args, **kwargs):
    return JSONReader(*args, **kwargs)
