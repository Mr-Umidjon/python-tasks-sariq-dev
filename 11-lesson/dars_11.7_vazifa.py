# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:13:56 2021

@author: WINDOWS 10
"""

son = int(input("Istalgan butun sonni kiriting "))
for n in range(2, 11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi ")