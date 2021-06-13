# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:05:32 2021

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
davlat = input("Davlat nomini kiriting ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]    
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
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
    


    