# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = dict(zip(header, row))
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for row in rows:
            try:
                prices[row[0]] = row[1]
            except IndexError:
                pass

    return prices

def calc_profit(portfolio, prices):
    profit = 0
    for i in portfolio:
        try:
            profit += ( float(prices[i['name']]) - float(i['price']) ) * float(i['shares'])
        except KeyError:
            import pdb; pdb.set_trace()

    return profit

def print_report(portfolio_f, prices_f):
    portfolio = read_portfolio(portfolio_f)
    prices = read_prices(prices_f)

    print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    print(('-'*10+' ')*4)

    for i in portfolio:
        change = ( float(prices[i['name']]) - float(i['price']) )
        print_data = (i["name"], i["shares"], "$"+prices[i["name"]], change)
        print('%10s %10s %10s %10.2f' % print_data)



print_report('Data/portfolio.csv', 'Data/prices.csv')

