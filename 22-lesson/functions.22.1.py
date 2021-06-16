# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:37:06 2021

@author: WINDOWS 10
"""

def kopaytma(*sonlar):
    """Sonlarni ko'paytmasini chiqaruvchi dastur"""
    kopayt = 1
    for son in sonlar:
        kopayt *= son
    return kopayt
print(kopaytma(12, 13))
print(kopaytma(1, 2, 3, 4, 5, 6, 7))    