#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            return "'{}'".format(self.value)

class SqlIntElement:
    def __init__(self, n):
        self.value = n

    def isit(s):
        if s.lower() == 'int':
            return SqlIntElement

    def __str__(self):
        return str(self.value)


ALL_ELEMENTS = (SqlTextElement, SqlIntElement)

def isit(s):
    for element in ALL_ELEMENTS:
        if element.isit(s):
            return element.isit(s)

