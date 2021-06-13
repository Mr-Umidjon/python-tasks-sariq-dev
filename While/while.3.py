# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:27:51 2021

@author: WINDOWS 10
"""

cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'nexia',\
        'malibu', 'nexia', 'tesla']
    
while "nexia" in cars:
    cars.remove('nexia')
    
cars.append('nexia')
for car in cars:
    print(car, end = ' ')




