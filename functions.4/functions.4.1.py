# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:14:58 2021

@author: WINDOWS 10
"""

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1, 2, 3, 4, 5))
print(summa(3, 4, 5, 6, 7, 45, 56, 67))
print(summa())
print(summa(1))
print(summa(54, 56, 7, 8))

