from Robinhood_Exporter import RobinhoodExporter, csv_export, json_export

if __name__ == '__main__':
 mfa = input("MFA Code? ")
 rh_export = RobinhoodExporter(mfa)
 stocks = rh_export.export_portfolio(csv_export('stocks.csv'))
