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

ALL_ELEMENTS = (SqlTextElement,)

def isit(s):
    for element in ALL_ELEMENTS:
        if element.isit(s):
            return element.isit(s)

