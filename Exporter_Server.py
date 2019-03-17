from flask import Flask, request, jsonify

from Robinhood_Exporter import RobinhoodExporter, LoginException

app = Flask(__name__)


@app.route("/", methods=['POST'])
def export_portfolio():
  req = request.get_json()
  print(req)

  if "rh_user" not in req:
    return "Username not passed in request\n"

  if "rh_pass" not in req:
    return "Password not passed in request\n"

  if "code" not in req:
    return "2factor code not passed in request\n"

  try:
    rh_user = req["rh_user"]
    rh_pass = req["rh_pass"]
    code = req["code"]
    stocks = RobinhoodExporter(code, rh_user, rh_pass).export_portfolio()
    return jsonify(stocks.as_dicts())
  except LoginException as err:
    return str(err) + "\n"
