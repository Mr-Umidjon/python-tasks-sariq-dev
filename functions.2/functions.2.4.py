# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:58:22 2021

@author: WINDOWS 10
"""

def oraliq(min, max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0, 10))
print(oraliq(10, 21))
print(oraliq(13, 345))


