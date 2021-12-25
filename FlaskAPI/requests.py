# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 00:11:29 2021

@author: ASUS
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Comtent-Type": "applicaton/json"}
data = {"input": data_in}

r = requests.get(URL, headers = headers, json = data)

r.json()