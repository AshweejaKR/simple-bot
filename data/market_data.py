# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import pandas as pd
import datetime as dt

import utils.utils


class market_data:

    def get_live_data(self):
        pass

    def get_hist_data(self, ticker, duration, interval, instrument_list, exchange="NSE"):
        params = {
            "exchange": exchange,
            "symboltoken": utils.utils.symbol_lookup(ticker, instrument_list),
            "interval": interval,
            "fromdate": (dt.date.today() - dt.timedelta(duration)).strftime('%Y-%m-%d %H:%M'),
            "todate": dt.date.today().strftime('%Y-%m-%d %H:%M')
        }
        hist_data = obj.getCandleData(params)
        df_data = pd.DataFrame(hist_data["data"],
                               columns=["date", "open", "high", "low", "close", "volume"])
        df_data.set_index("date", inplace=True)
        df_data.index = pd.to_datetime(df_data.index)
        df_data.index = df_data.index.tz_localize(None)
        return df_data