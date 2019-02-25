from Robinhood import Robinhood
import os
import time
from random import uniform
import csv, json
import dateutil.parser as dateparser

from Stock import Stock
from Portfolio import Portfolio


def csv_export(filename):
  def export(portfolio):
    stocks = portfolio.as_dicts()['stocks']
    with open(filename, 'w') as f:
      if len(stocks) == 0:
        return

      writer = csv.DictWriter(f, stocks[0].keys())
      writer.writeheader()
      for stock in stocks:
        writer.writerow(stock)

  return export


def json_export(filename):
  def export(portfolio):
    stocks = portfolio.as_dicts()['stocks']
    with open(filename, 'w') as f:
      f.write(json.dumps(stocks, indent=2))

  return export


class RobinhoodExporter:
  def __init__(self, mfa_code):
    username = os.environ['rh_user']
    password = os.environ['rh_pass']

    self.rh = Robinhood()
    if not self.rh.login(username, password, mfa_code):
      raise Error("Invalid login credentials.")

  def _stock_from_security(self, security):
    stock = self.rh.get_url(security['instrument'])
    quote = self.rh.get_url(stock['quote'])

    ticker          = stock['symbol']
    quoted_equity   = round(float(quote['last_trade_price']), 2)
    quoted_datetime = dateparser.parse(quote['updated_at'])
    avg_cost        = round(float(security['average_buy_price']), 2)
    quantity        = round(float(security['quantity']), 2)

    return Stock(ticker, quoted_equity, quoted_datetime, avg_cost, quantity)
  
  def export_portfolio(self, export_func=None):
    securities = self.rh.securities_owned()

    stocks = []
    for security in securities['results']:
      stocks.append(self._stock_from_security(security))
      time.sleep(uniform(0.5, 2))

    total_equity = self.rh.equity()
    portfolio = Portfolio(total_equity, stocks)

    if export_func:
      export_func(portfolio)
    return portfolio
