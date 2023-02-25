from flask_restful import Resource
from flask import request
from functions.trade import order
from models import TradeData


class MakeTrade(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        
        trade = TradeData(
         symbol = json_data['symbol'], 
        qty = json_data['qty'],
        side = json_data['side'],
        _type = json_data['type'], 
        time_in_force = json_data['time_in_force']
        )

        try:    
            result = order(trade.symbol, trade.qty, trade.side, trade._type, trade.time_in_force)
            return {"status": 'success', 'data': result}, 201
        except:
            return {"Messege" : "No user with that api key"}, 402