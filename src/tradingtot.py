# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import threading
import time

from utils import SmartAPI


class Task:
    def __init__(self, name, interval, function):
        self.name = name
        self.interval = interval
        self.function = function
        self.stop_event = threading.Event()
        self.trade = "NA"
        self.isOpen = False
        self.no_of_exec = 0

    def execute(self):
        while not self.stop_event.is_set():
            r = self.function()

            if r == "BUY" and self.trade != 'BUY':
                if self.isOpen:
                    self.trade = 'NA'
                    self.isOpen = False
                    print("exiting short Trade ...")
                    self.no_of_exec = self.no_of_exec + 1
                else:
                    self.trade = "BUY"
                    self.isOpen = True
                    print("entering Long Trade ...")

            elif r == "SELL" and self.trade != 'SELL':
                if self.isOpen:
                    self.trade = 'NA'
                    self.isOpen = False
                    print("exiting Long Trade ...")
                    self.no_of_exec = self.no_of_exec + 1
                else:
                    self.trade = "SELL"
                    self.isOpen = True
                    print("entering short Trade ...")

            time.sleep(self.interval)

    def stop(self):
        self.stop_event.set()


def running_disp():
    print("Bot Scheduler running ...")


class Scheduler:
    # class attribute
    is_running = False

    def __init__(self):
        self.tasks = []
        self.add_task("self", 5, running_disp)

    def add_task(self, name, interval, function):
        task = Task(name, interval, function)
        self.tasks.append(task)

    def run(self):
        if not self.__class__.is_running:
            for task in self.tasks:
                thread = threading.Thread(target=task.execute)
                thread.start()
            self.__class__.is_running = True
        else:
            print("bot already running ...")

    def stop(self, msg=None):
        print("stopping trading bot, msg: {} ".format(msg))
        self.__class__.is_running = False
        for task in self.tasks:
            task.stop()


class Tradingtot(Scheduler):
    def __init__(self):
        self.obj = None

        # invoking the __init__ of the parent class
        Scheduler.__init__(self)

    def config(self):
        # just for testing
        key_secret = open("D:\\GitHub\\simple-bot\\utils\\key.txt", "r").read().split()
        api_key = key_secret[0]
        api_secret = key_secret[1]
        client_id = key_secret[2]
        passwd = key_secret[3]
        totp_str = key_secret[4]

        self.obj = SmartAPI(api_key, api_secret, client_id, passwd, totp_str)
        self.obj.login()

    def exit(self):
        self.obj.logout()
