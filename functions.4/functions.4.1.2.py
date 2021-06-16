# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:24:26 2021

@author: WINDOWS 10
"""

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)
print(summa(3, 4, 5, 6, 7, 45, 56, 67))
print(summa())
print(summa(1))
print(summa(54, 56, 7, 8))
