#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of json-append.
# https://github.com/SeedyROM/json-append

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

from preggy import expect

from json_append import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
