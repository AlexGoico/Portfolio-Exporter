class Portfolio:
  def __init__(self, total_equity, stocks):
    self.total_equity = total_equity
    self.total_avg_cost = sum(stock.avg_cost for stock in stocks)
    self.stocks = stocks

  def get_avgprice_to_portfolio(self, stock):
    return round(stock.avg_cost / self.total_avg_cost, 5)
  
  def get_avgequity_to_portfolio(self, stock):
    return round(stock.quoted_equity / self.total_equity, 5)

  def as_dicts(self):
    ret = {
      'total_equity'    : self.total_equity,
      'total_avg_price' : self.total_avg_cost,
      'stocks'          : []
    }

    for stock in self.stocks:
      stock_dict = stock.__dict__
      stock_dict['avgprice_portfolio_ratio'] = self.get_avgprice_to_portfolio(stock)
      stock_dict['avgequity_portfolio_ratio'] = self.get_avgequity_to_portfolio(stock)

      ret['stocks'].append(stock_dict)

    return ret

  def __repr__(self):
    return f"Portfolio({self.total_equity}, {self.total_avg_cost}, {self.stocks})"
