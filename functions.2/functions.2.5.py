# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:07:59 2021

@author: WINDOWS 10
"""

def oraliq(min, max, qadam = 1):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar

print(oraliq(0, 10, 3))
print(oraliq(10, 21, 4))



