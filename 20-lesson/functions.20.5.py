# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:37:14 2021

@author: WINDOWS 10
"""

def fibonochchi(son):
    sonlar = []
    for x in range(son):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar
        
sonlar = fibonochchi(1000) 


