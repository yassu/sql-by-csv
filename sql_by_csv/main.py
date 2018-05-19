#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import csv
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import insert_sql, elements

def get_row_elements(row, types):
    for i, item in enumerate(row):
        _type = elements.isit(types[i])
        yield _type(item)

def main():
    filename = 'example_insert.csv'

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader)
        print('cols: {}'.format(cols))
        types = next(reader)
        print('types: {}'.format(types))
        table_name = 'TableName'    # TODO: コマンドラインの引数から取るようにする

        for row in reader:
            print(
                str(insert_sql.InsertQuery(table_name,
                    cols,
                    list(get_row_elements(row, types))
                ))
            )

if __name__ == '__main__':
    main()
