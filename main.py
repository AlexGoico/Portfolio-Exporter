from Portfolio_Exporter.Robinhood_Exporter import RobinhoodExporter, csv_export, json_export
from pprint import pprint

def export(portfolio):
  filename = "stocks"
  csv_export(f"out/{filename}.csv")(portfolio)
  json_export(f"out/{filename}.json")(portfolio)

if __name__ == '__main__':
 mfa = input("MFA Code? ")
 rh_export = RobinhoodExporter(mfa)
 portfolio = rh_export.export_portfolio(export)
 pprint(portfolio.as_dicts())
