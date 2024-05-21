# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import sys

from src import Tradingtot
from data import market_data

from utils.logger import *

bot_mode = "LIVE"

def main():
    # Example tasks/functions
    def trading_strategy1():
        lg.info("trading_strategy1 is running")
        # running for test ##
        ticker = "INFY"
        obj = market_data()
        data = obj.get_current_price(ticker)
        print(data)

        infy_data = obj.get_hist_data("INFY", 5, "ONE_DAY")
        lg.info(infy_data)
        # end test ###

    # initialize the logger (imported from logger)
    initialize_logger()

    # Create an instance of TradingBot
    bot = Tradingtot()

    # add strategy as Task to the TradingBot
    bot.add_task("Task 1", 2, trading_strategy1)

    # running the TradingBot
    bot.run()

if __name__ == "__main__":
    main()
