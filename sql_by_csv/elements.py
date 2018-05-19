#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import utils

class SqlVarcharElement:
    def __init__(self, s):
        self.value = s

    @staticmethod
    def isit(s):
        # TODO: varchar, varchar max, varchar(50)などに対応する
        if s.lower() == 'varchar':
            return SqlVarcharElement

    def __str__(self):
        if self.value.lower() == 'null':
            return 'null'
        else:
            return utils.str_escape(self.value)

class SqlTextElement:
    def __init__(self, s):
        self.value = s

    @staticmethod
    def isit(s):
        if s.lower() == 'text':
            return SqlTextElement

    def __str__(self):
        # TODO: エスケープシーケンスを考慮する
        if self.value.lower() == 'null':
            return 'null'
        else:
            return utils.str_escape(self.value)

class SqlIntElement:
    def __init__(self, n):
        self.value = n

    def isit(s):
        if s.lower() == 'int':
            return SqlIntElement

    def __str__(self):
        return str(self.value)

class SqlDatetimeElement:
    def __init__(self, d):
        self.value = d

    @staticmethod
    def isit(s):
        if s.lower() == 'datetime':
            return SqlDatetimeElement

    def __str__(self):
        return "'{}'".format(self.value)


ALL_ELEMENTS = (
    SqlTextElement,
    SqlIntElement,
    SqlVarcharElement,
    SqlDatetimeElement,
)

def isit(s):
    for element in ALL_ELEMENTS:
        if element.isit(s):
            return element.isit(s)

