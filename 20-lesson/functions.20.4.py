# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:11:48 2021

@author: WINDOWS 10
"""

def tub_sonlar_top(min, max):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
    tub_sonlar = []
    for n in range(min, max+1):
        tub = True
        if (n == 1):
            tub = False
        elif  (n == 2):
            tub = True
        else:
            for x in range(2, n):
                if (n % x == 0):
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar         
   