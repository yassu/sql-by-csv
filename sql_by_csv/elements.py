#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SqlStringElement:
    def __init__(self, s):
        self.value = s

    @staticmethod
    def isit(s):
        if s.lower() == 'string':
            return SqlStringElement

    def __str__(self):
        # TODO: エスケープシーケンスを考慮する
        return "'{}'".format(self.value)

ALL_ELEMENTS = (SqlStringElement,)

def isit(s):
    for element in ALL_ELEMENTS:
        if element.isit(s):
            return element.isit(s)

