import requests, json, collections
import pandas as pd
import time

alpaca_key = 'PK3HZ7GP4ZDFHZYGFUF5'
secret_key = 'v5OgSGltMMYVgzcJdr4qIrNJi6095i3LcjNrxo6p'
td_key = 'SOYXE4023VBYCAWGRM138ATII6MKXGZ9'


alpaca_base_url = "https://paper-api.alpaca.markets"
order_url = f"{alpaca_base_url}/v2/orders"
headers = {"APCA-API-KEY-ID": alpaca_key, "APCA-API-SECRET-KEY": secret_key}


def order(symbol, qty, side, type, time_in_force):
   parameters = {
   "symbol": symbol,
   "qty": qty,
   "side": side,
   "type": type,
   "time_in_force": time_in_force,
   }
   request = requests.post(order_url, json=parameters, headers=headers)
   return json.loads(request.content)
