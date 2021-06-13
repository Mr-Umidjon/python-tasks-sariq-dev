# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:50:31 2021

@author: WINDOWS 10
"""

def bolinish_alomatlari(son):
    """Sonni bo'linish alomatlarini tekshiruvchi funksiya """
    for n in range(1,11):
        if not son % (n):
            print(f"{son} {n} ga qoldiqsiz bo'linadi ")

bolinish_alomatlari(24)
