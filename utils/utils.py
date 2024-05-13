# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import datetime as dt
from datetime import time

import pytz


def utility():
    pass


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
