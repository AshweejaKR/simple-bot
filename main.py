# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import time, sys

from src import Tradingtot
from utils.utils import is_market_open, wait_till_market_open
from data import market_data
from data import global_data

bot_mode = "LIVE"

def main():
    # Example tasks/functions
    def task1():
        print("Task 1 is running")
        ticker = "INFY"
        data = market_data()
        data.get_live_data(ticker)
        
        infy_data = data.get_hist_data("INFY", 10, "ONE_MINUTE")

        for i in range(1,len(infy_data[1:])):
            print(infy_data.iloc[i]["close"])

    def task2():
        print("Task 2 is running")

    # Create an instance of TradingBot
    bot = Tradingtot()

    # config the TradingBot
    obj = bot.config()
    print("main:35 obj : ", obj)

    bot.add_task("Task 1", 2, task1)
    # bot.add_task("Task 2", 3, task2)

    wait_till_market_open()

    # running the TradingBot
    bot.run()

    print("is_market_open: ", is_market_open())
    c = 0
    try:
        while bot.is_running:
            time.sleep(1)
            c = c + 1

            if not is_market_open():
                bot.stop("Market Closed")

            elif c > 10:
                bot.stop("Max run hit")
    except KeyboardInterrupt:
        bot.stop("bot stop request by user")

    bot.exit()
    print("Trading bot done ...")


if __name__ == "__main__":
    main()
