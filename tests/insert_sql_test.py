#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import insert_sql, elements


class TestSqlInsertQuery(unittest.TestCase):

    def test_init(self):
        insert_sql.InsertQuery('TableName',
            ('col1', 'col2'), ('val1', 'val2'))

    def test_str(self):
        self.assertEqual(
            str(insert_sql.InsertQuery('TableName',
                ('col1', 'col2'),
                (elements.SqlStringElement('val1'), elements.SqlStringElement('val2'))
            )),
            "INSERT INTO [TableName] (col1, col2) VALUES('val1', 'val2');")


if __name__ == "__main__":
    unittest.main()
