# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import datetime as dt
from datetime import time

import pytz


def token_lookup(ticker, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[
            -1] == "EQ":
            return instrument["token"]


def symbol_lookup(token, instrument_list, exchange="NSE"):
    for instrument in instrument_list:
        if instrument["token"] == token and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[
            -1] == "EQ":
            return instrument["name"]


def is_market_open(mode='None'):
    if mode != "TEST":
        start_time = dt.time(9, 16)
        end_time = dt.time(15, 16)
    else:
        start_time: time = dt.time(0, 0)
        end_time: time = dt.time(23, 59)
    cur_time = dt.datetime.now(pytz.timezone("Asia/Kolkata")).time()
    if start_time <= cur_time <= end_time:
        return True
    else:
        return False
