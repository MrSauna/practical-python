# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    header = next(rows)

    sum = 0

    for lineno, row in enumerate(rows, 1):
        try:
            record = dict(zip(header, row))
            sum += int(record['shares']) * float(record['price'])
        except ValueError:
            print('Encoutered ValueError', 'line', lineno, row)
            pass

    return sum
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
