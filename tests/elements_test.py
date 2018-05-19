#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import elements

class TestSqlTextElement(unittest.TestCase):

    def test_init(self):
        elements.SqlTextElement("abc")

    def test_to_string(self):
        self.assertTrue(str(elements.SqlTextElement("abc")) == "'abc'")

    def test_to_string2(self):
        self.assertTrue(str(elements.SqlTextElement("null")) == "null")

    def test_to_string3(self):
        self.assertTrue(str(elements.SqlTextElement("Null")) == "null")

    def test_isit(self):
        self.assertTrue(elements.SqlTextElement.isit('text'))

    def test_isit2(self):
        self.assertTrue(elements.SqlTextElement.isit('Text'))

    def test_isit3(self):
        self.assertFalse(elements.SqlTextElement.isit('xyz'))

class TestSqlIntElement(unittest.TestCase):
    def test_init(self):
        elements.SqlIntElement(3)

    def test_isit(self):
        self.assertTrue(elements.SqlIntElement.isit('int'))

    def test_isit2(self):
        self.assertTrue(elements.SqlIntElement.isit('Int'))

    def test_isit3(self):
        self.assertFalse(elements.SqlIntElement.isit('string'))

    def test_str(self):
        self.assertTrue(str(elements.SqlIntElement(6)) == '6')

class TestRawFunctions(unittest.TestCase):
    def test_isit(self):
        self.assertTrue(elements.isit('Text') == elements.SqlTextElement)

    def test_isit2(self):
        self.assertTrue(elements.isit('Int') == elements.SqlIntElement)


if __name__ == "__main__":
    unittest.main()
