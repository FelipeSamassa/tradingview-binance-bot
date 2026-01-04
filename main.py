from flask import Flask, request
from binance.client import Client
import os

app = Flask(__name__)

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

client = Client(api_key, api_secret)

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
