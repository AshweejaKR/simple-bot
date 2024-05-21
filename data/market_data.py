# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import pandas as pd
import datetime as dt

import utils.utils
from data import global_data
from utils.logger import *


class market_data:
    def __init__(self):
        self.obj = global_data.smartapi_obj

    def get_live_data(self, ticker, exchange='NSE'):
        data = self.obj.ltpData(exchange=exchange, tradingsymbol=ticker, symboltoken=utils.utils.token_lookup(ticker))
        return data

    def get_current_price(self, ticker, exchange='NSE'):
        data = self.get_live_data(ticker, exchange)
        if data['status'] and (data['message'] == 'SUCCESS'):
            ltp = float(data['data']['ltp'])
            return ltp

        else:
            template = "An ERROR occurred. error message : {0!r}"
            message = template.format(data['message'])
            lg.error(message)

    def get_hist_data(self, ticker, duration, interval, exchange="NSE"):
        params = {
            "exchange" : exchange,
            "symboltoken" : utils.utils.token_lookup(ticker),
            "interval" : interval,
            "fromdate" : (dt.date.today() - dt.timedelta(duration)).strftime('%Y-%m-%d %H:%M'),
            "todate" : dt.date.today().strftime('%Y-%m-%d %H:%M')
        }

        hist_data = self.obj.getCandleData(params)
        df_data = pd.DataFrame(hist_data["data"],
                               columns=["date", "open", "high", "low", "close", "volume"])
        df_data.set_index("date", inplace=True)
        df_data.index = pd.to_datetime(df_data.index)
        df_data.index = df_data.index.tz_localize(None)
        return df_data