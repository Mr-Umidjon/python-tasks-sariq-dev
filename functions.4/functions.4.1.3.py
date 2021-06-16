# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:25:28 2021

@author: WINDOWS 10
"""

def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x + y + sum(sonlar)
print(summa(3, 4, 5, 6, 7, 45, 56, 67))
print(summa(345, 567))
print(summa(1, 3))
print(summa(54, 56, 7, 8))
