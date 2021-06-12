# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:55:31 2021

@author: WINDOWS 10
"""

#Lug'at ichida ro'yxat
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    "maryam":['c++', 'c#']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:",end = ' ')
    for til in tillar:
         print(f'{til.upper()}',end = ' ')
         
         
         
         
         
         