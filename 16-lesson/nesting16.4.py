# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:55:37 2021

@author: WINDOWS 10
"""

davlatlar = {
    "o'zbekiston":{
        'poytaxt':'toshkent',
        'hudud':448978,
        'aholi':33000000,
        'pul birlig':"so'm"},
    "rossiya":{
        'poytaxt':'moskva',
        'hudud':17098246,
        'aholi':144000000,
        'pul birlig':"rubl"},
    "aqsh":{
        'poytaxt':'vashington',
        'hudud':9631418,
        'aholi':327000000,
        'pul birlig':"dollar"},
    "malayziya":{
        'poytaxt':'kuala-lumpur',
        'hudud':329750,
        'aholi':25000000,
        'pul birlig':"rinngit"},
    }
for davlat, info in davlatlar.items():
    if davlat.lower() == 'aqsh':
        davlat = davlat.upper()
        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}\n",
             f"Hududi: {info['hudud']} kv.km\n",
             f"Aholisi: {info['aholi']}\n",
             f"Pul birligi: {info['pul birlig']}")
    else:
        davlat = davlat.capitalize()
        print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}\n",
              f"Hududi: {info['hudud']} kv.km\n",
              f"Aholisi: {info['aholi']}\n",
              f"Pul birligi: {info['pul birlig']}")







