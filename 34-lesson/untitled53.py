# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:49:00 2021

@author: WINDOWS 10
"""

from pprint import pprint
import json


filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
pprint(bemor)