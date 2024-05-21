# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:05 2024

@author: ashwe
"""

import urllib
import json

from SmartApi import SmartConnect
from pyotp import TOTP

from data import global_data

class SmartAPI:
    def __init__(self, api_key, api_secret, client_id, passwd, totp_str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client_id = client_id
        self.passwd = passwd
        self.totp_str = totp_str
        self.obj = None

        # Initialize SmartAPI connection
        self.obj = SmartConnect(api_key = self.api_key)
        global_data.smartapi_obj = self.obj
        print("smart api:28 obj : ", self.obj)

        instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = urllib.request.urlopen(instrument_url)
        global_data.instrument_list = json.loads(response.read())

    def get_smartapi_obj(self):
        print("smart api:34 obj : ", self.obj)
        return self.obj

    def login(self):
        # Login to the SmartAPI
        try:
            data = self.obj.generateSession(self.client_id, self.passwd, TOTP(self.totp_str).now())
            if(data['status'] and data['message'] == 'SUCCESS'):
                print('Login success ... !')
            else:
                print('Login failed ... !')
        except Exception as err:
            template = "An exception of type {0} occurred. error message:{1!r}"
            message = template.format(type(err).__name__, err.args)
            print("ERROR: {}".format(message))

    def logout(self):
        # Logout from the SmartAPI
        try:
            data = self.obj.terminateSession(self.client_id)
            if(data['status'] and data['message'] == 'SUCCESS'):
                print('Logout success ... !')
            else:
                print('Logout failed ... !')
        except Exception as err:
            template = "An exception of type {0} occurred. error message:{1!r}"
            message = template.format(type(err).__name__, err.args)
            print("ERROR: {}".format(message))
            print('Logout failed ... !')

    def place_order(self, symbol, price, quantity, order_type):
        # Place order using SmartAPI
        pass
