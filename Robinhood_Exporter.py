from Robinhood import Robinhood
import os
import time
import csv, json

from Stock import Stock

def csv_export(filename):
  def export(stocks):
    with open(filename, 'w') as f:
      if len(stocks) == 0:
        return

      stocks = [stock.__dict__ for stock in stocks]
      writer = csv.DictWriter(f, stocks[0].keys())
      writer.writeheader()
      for stock in stocks:
        writer.writerow(stock)

  return export

def json_export(filename):
  def export(stocks):
    stocks = [stock.__dict__ for stock in stocks]
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

  def _stock_from_security(self, total_equity, security):
    stock = self.rh.get_url(security['instrument'])

    ticker       = stock['symbol']
    avg_price    = round(float(security['average_buy_price']), 2)
    quantity     = round(float(security['quantity']), 2)
    equity       = round(avg_price*quantity, 2)
    port_percent = round(equity / total_equity, 2)

    return Stock(ticker, equity, avg_price, quantity, port_percent)
  
  def export_portfolio(self, export_func=print):
    securities = self.rh.securities_owned()

    stocks = []
    total_equity = self.rh.equity()
    for security in securities['results']:
      stocks.append(self._stock_from_security(total_equity, security))
      time.sleep(1)
    
    export_func(stocks)
    return stocks
 