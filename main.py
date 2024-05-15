# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import time

from src import Tradingtot
from utils.utils import is_market_open


def main():
    # Example tasks/functions
    def task1():
        print("Task 1 is running")

    def task2():
        print("Task 2 is running")

    # Create an instance of TradingBot
    bot = Tradingtot()

    # config the TradingBot
    bot.config()

    bot.add_task("Task 1", 2, task1)
    bot.add_task("Task 2", 3, task2)

    # running the TradingBot
    bot.run()

    print("is_market_open: ", is_market_open())
    try:
        while bot.is_running:
            time.sleep(1)

            if not is_market_open():
                bot.stop("Market Closed")
    except KeyboardInterrupt:
        bot.stop("bot stop request by user")

    bot.exit()
    print("Trading bot done ...")


if __name__ == "__main__":
    main()
