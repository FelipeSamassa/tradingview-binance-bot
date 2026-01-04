from flask import Flask, request
from binance.client import Client

API_KEY = "SjI1fY8OJizUfo1f74KSwR1Zjm9fKHTlEPCgMvd5huKBgMwPyccUxZwKRvZm2UMA"
API_SECRET = "SfrxIXHGXc609ZQh4lLtdHG2LnMdh9fVP4p87D9gv9XbnFnh4IR8BoTxpLmqqVNr"

client = Client(API_KEY, API_SECRET)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot online"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    symbol = data["symbol"]
    side = data["side"]
    quantity = float(data["quantity"])

    order = client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return {"status": "ok", "order": order}

app.run(port=5000)
