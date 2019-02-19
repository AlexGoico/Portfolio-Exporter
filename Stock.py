class Stock:
  def __init__(self, ticker, equity, avg_cost, quantity, percentage):
    self.ticker = ticker
    self.equity = equity
    self.avg_cost = avg_cost
    self.quantity = quantity
    self.rh_port_percentage = percentage