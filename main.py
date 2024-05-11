# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

from src import tradingtot

def main():
    # Create an instance of TradingBot
    bot = tradingtot()

    # config the TradingBot
    bot.config()

    # running the TradingBot
    bot.run()
    
if __name__ == "__main__":
    main()