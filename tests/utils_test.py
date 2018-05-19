#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import utils

class TestUtils(unittest.TestCase):
    def test_str_escape(self):
        self.assertEqual(utils.str_escape('abc'), "'abc'")

    def test_str_escape2(self):
        self.assertEqual(
            utils.str_escape("abc'def'klm'stu"),
            "'abc''def''klm''stu'")


if __name__ == "__main__":
    unittest.main()
