#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SqlStringElement:
    def __init__(self, s):
        self.value = s

    def __str__(self):
        # TODO: エスケープシーケンスを考慮する
        return "'{}'".format(self.value)