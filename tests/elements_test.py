#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import elements

class TestSqlStringElement(unittest.TestCase):

    def test_init(self):
        elements.SqlStringElement("abc")

    def test_to_string(self):
        self.assertTrue(str(elements.SqlStringElement("abc")) == "'abc'")

    def test_isit(self):
        self.assertTrue(elements.SqlStringElement.isit('string'))

    def test_isit2(self):
        self.assertTrue(elements.SqlStringElement.isit('String'))

    def test_isit3(self):
        self.assertFalse(elements.SqlStringElement.isit('xyz'))


class TestRawFunctions(unittest.TestCase):
    def test_isit(self):
        self.assertTrue(elements.isit('String') == elements.SqlStringElement)


if __name__ == "__main__":
    unittest.main()
