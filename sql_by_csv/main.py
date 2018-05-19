#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import csv
from optparse import OptionParser
import sys,os
sys.path.append(os.path.expanduser('./../sql_by_csv/'))
from sql_by_csv import insert_sql, elements

def get_row_elements(row, types):
    for i, item in enumerate(row):
        _type = elements.isit(types[i])
        yield _type(item)

def get_parser():
    parser = OptionParser()
    parser.add_option(
        '--table-name', '-t',
        action='store',
        dest='table_name',
        type='string',
        help='table name'
    )
    parser.add_option(
        '--csv-filename', '-c',
        action='store',
        dest='csv_filename',
        type='string',
        help='csv filename'
    )
    return parser

def main():
    opts, args = get_parser().parse_args()

    # TODO: table_nameがNoneだったらError
    # TODO: csv_filenameがNoneだったらError

    with open(opts.csv_filename, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader)
        types = next(reader)

        for row in reader:
            print(
                str(insert_sql.InsertQuery(opts.table_name,
                    cols,
                    list(get_row_elements(row, types))
                ))
            )

if __name__ == '__main__':
    main()
