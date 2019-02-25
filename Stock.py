class Stock:
  def __init__(self, ticker, quoted_equity, quote_datetime, avg_cost, quantity):
    self.ticker = ticker
    self.quoted_equity = quoted_equity
    self.quote_datetime = quote_datetime.isoformat()
    self.avg_cost = avg_cost
    self.quantity = quantity

  def __repr__(self):
    pass
