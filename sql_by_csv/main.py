#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import csv
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import insert_sql, elements

def main():
    filename = 'example_insert.csv'

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader)
        print('cols: {}'.format(cols))
        # TODO: 自動でtypeに対してElementsを取得するようにする
        types = next(reader)
        print('types: {}'.format(types))
        table_name = 'TableName'    # TODO: コマンドラインの引数から取るようにする

        for row in reader:
            print(
                str(insert_sql.InsertQuery(table_name,
                    ('col1', 'col2'),
                    (elements.SqlStringElement('val1'), elements.SqlStringElement('val2'))
                ))
            )

if __name__ == '__main__':
    main()
