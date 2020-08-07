# fileparse.py
#
# Exercise 3.3

import csv
import pdb

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        def my_format(key, val):
            if key == 'shares':
                return int(val)
            elif key == 'price':
                return float(val)
            else:
                return val

        if has_headers: # create a dict
            headers = next(rows)

        for row in rows:
            if not row: # skip empty
                continue

            if has_headers:
                #pdb.set_trace()
                record = dict(zip(headers, row))

                if select: # select defined fields
                    record = {s: record[s] for s in record if s in select}
                # format values to make sense
                record = {s:my_format(s, record[s]) for s in record}

            else: # no header make a tuple
                record = tuple(func(value) for value, func in zip(row, types))

            records.append(record)

    return records

#portfolio = parse_csv('Data/portfolio.csv', select=('name','shares'))
#portfolio = parse_csv('Data/prices.csv', has_headers=False, types=(str,float))
portfolio = parse_csv('Data/portfolio.dat', delimiter=' ')
print(portfolio)
