# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:11:14 2021

@author: WINDOWS 10
"""

#Ro'yxat ichida lug'at
car0 = {
        'model':'lacetti',
        'rang':'oq',
        "yil":2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }
car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':"maexanika"
        }
car2 = {
        'model':"gentra",
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':"mexanika"
        }
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']} $" )
    



















    