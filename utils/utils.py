# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import datetime as dt
import time
import pytz
import sys
from data import global_data


def token_lookup(ticker, exchange="NSE"):
    for instrument in global_data.instrument_list:
        if instrument["name"] == ticker and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[
            -1] == "EQ":
            return instrument["token"]


def symbol_lookup(token, exchange="NSE"):
    for instrument in global_data.instrument_list:
        if instrument["token"] == token and instrument["exch_seg"] == exchange and instrument["symbol"].split('-')[
            -1] == "EQ":
            return instrument["name"]


def wait_till_market_open():
    while True:
        cur_time = dt.datetime.now(pytz.timezone("Asia/Kolkata")).time()
        if cur_time > global_data.endTime or cur_time < global_data.waitTime:
            print('Market is closed. \n')
            sys.exit()

        if cur_time > global_data.startTime:
            break

        print("Market is NOT opened waiting ... !")
        time.sleep(global_data.sleepTime)

    print("Market is Opened ...")


def is_market_open(mode='None'):
    cur_time = dt.datetime.now(pytz.timezone("Asia/Kolkata")).time()
    if global_data.startTime <= cur_time <= global_data.endTime:
        return True
    else:
        return False
