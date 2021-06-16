# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:36:06 2021

@author: WINDOWS 10
"""

def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

tub_sonlar = list(filter(tubmi, range(100)))
print(tub_sonlar)
