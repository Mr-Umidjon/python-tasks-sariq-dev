# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:28:00 2021

@author: WINDOWS 10
"""

import random as r
sonlar = r.sample(range(100), 10)
print(sonlar)

#def juftmi(x):
#    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
#    return x % 2 == 0

#juft_sonlar = list(filter(juftmi, sonlar))
#print(juft_sonlar)

juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))
print(juft_sonlar)