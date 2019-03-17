import dateutil.parser as dateparser

class Stock:
  def __init__(self, ticker, quoted_equity, quote_datetime, avg_cost, quantity):
    self.ticker = ticker
    self.quoted_equity = quoted_equity
    self.quote_datetime = quote_datetime.isoformat()
    self.avg_cost = avg_cost
    self.quantity = quantity

  def __repr__(self):
    return f"Stock({self.ticker}, {self.quoted_equity}, {self.quote_datetime}, {self.avg_cost}, {self.quantity})"

  @staticmethod
  def from_security_and_quote(security, quote, precision=2):
    ticker = quote['symbol']
    quoted_equity = round(float(quote['last_trade_price']), precision)
    quoted_datetime = dateparser.parse(quote['updated_at'])
    avg_cost = round(float(security['average_buy_price']), precision)
    quantity = round(float(security['quantity']), precision)

    return Stock(ticker, quoted_equity, quoted_datetime, avg_cost, quantity)
