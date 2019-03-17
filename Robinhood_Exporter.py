from Robinhood import Robinhood
import os
import csv, json

from Stock import Stock
from Portfolio import Portfolio


def quote_endpoint(securities):
  return f'https://api.robinhood.com/marketdata/quotes/?instruments=' \
    f'{",".join([security["instrument"] for security in securities])}'


class LoginException(Exception):
  pass


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
  """
  Exports metadata about a Robinhood user's held securities and portfolio.
  """

  def __init__(self, mfa_code, username=None, password=None):
    username = os.environ['rh_user'] if None else username
    password = os.environ['rh_pass'] if None else password

    try:
      self.rh = Robinhood()
      if not self.rh.login(username, password, mfa_code):
        raise LoginException("Invalid login credentials.")
    except:
      raise LoginException("Invalid login credentials.")

  def _securities_to_quotes(self, securities):
    return self.rh.get_url(quote_endpoint(securities))['results']

  def _stocks_from_securities(self, securities):
    for security, quote in zip(securities, self._securities_to_quotes(securities)):
      yield Stock.from_security_and_quote(security, quote)

  def export_portfolio(self, export_func=None):
    securities = self.rh.securities_owned()

    stocks = list(self._stocks_from_securities(securities['results']))

    total_equity = self.rh.equity()
    portfolio = Portfolio(total_equity, stocks)

    if export_func:
      export_func(portfolio)
    return portfolio
