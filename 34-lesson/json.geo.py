# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:07:40 2021

@author: WINDOWS 10
"""

import json
import googlemaps
from apikey import APIKEY


gmaps = googlemaps.Client(key = APIKEY)

data = gmaps.geocode("Olmazor", "Tashkent", "Uzbekistan")


g = json.dumps(data[0], indent=4, sort_keys=True)
print(g)