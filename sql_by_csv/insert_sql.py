#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InsertQuery:
    def __init__(self, table_name, col_names, vals):
        self._table_name = table_name
        self._col_names = col_names
        self._vals = vals

    def __str__(self):
        query = "INSERT INTO [{}] ".format(self._table_name)
        query += '({}) '.format(', '.join(self._col_names))
        val_strs = tuple(map(lambda x: str(x), self._vals))
        query += 'VALUES({});'.format(', '.join(val_strs))
        return query
