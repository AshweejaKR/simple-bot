# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import sys

from src import Tradingtot
from data import market_data

bot_mode = "LIVE"

def main():
    # Example tasks/functions
    def trading_strategy1():
        print("trading_strategy1 is running")
        # running for test ##
        ticker = "INFY"
        data = market_data()
        data.get_live_data(ticker)
        
        infy_data = data.get_hist_data("INFY", 5, "ONE_DAY")
        print(infy_data)
        # end test ###

    # Create an instance of TradingBot
    bot = Tradingtot()

    # add strategy as Task to the TradingBot
    bot.add_task("Task 1", 2, trading_strategy1)

    # running the TradingBot
    bot.run()

if __name__ == "__main__":
    main()
