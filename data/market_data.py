# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import pandas as pd
import datetime as dt

import utils.utils
from data import global_data


class market_data:
    def __init__(self):
        self.obj = global_data.smartapi_obj
        print("market data:18 obj : ", self.obj)

    def get_live_data(self):
        pass

    def get_hist_data(self, ticker, duration, interval, exchange="NSE"):
        print("global_data.instrument_list : ", global_data.instrument_list)
        params = {
            "exchange" : exchange,
            "symboltoken" : utils.utils.token_lookup(ticker),
            "interval" : interval,
            "fromdate" : (dt.date.today() - dt.timedelta(duration)).strftime('%Y-%m-%d %H:%M'),
            "todate" : dt.date.today().strftime('%Y-%m-%d %H:%M')
        }

        print("params: ", params)
        print("market data:34 obj : ", self.obj)
        hist_data = self.obj.getCandleData(params)
        print("hist_data: ", hist_data)
        df_data = pd.DataFrame(hist_data["data"],
                               columns=["date", "open", "high", "low", "close", "volume"])
        df_data.set_index("date", inplace=True)
        df_data.index = pd.to_datetime(df_data.index)
        df_data.index = df_data.index.tz_localize(None)
        return df_data