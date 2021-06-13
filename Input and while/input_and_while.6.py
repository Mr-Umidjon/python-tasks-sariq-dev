# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 23:10:34 2021

@author: WINDOWS 10
"""

son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son, end = ' ')
        