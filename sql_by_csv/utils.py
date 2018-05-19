#!/usr/bin/env python
# -*- coding: utf-8 -*-

def str_escape(s):
    return "'{}'".format(s.replace("'", "''"))
