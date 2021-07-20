# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 08:29:26 2021

@author: WINDOWS 10
"""

def maxSon(a, b, c):
    return max(a, b, c)

def katt_matn(royxat):
    return [matn.title() for matn in royxat]

def juftSon(sonlar):
    juft_sonlar = []
    for son in sonlar:
        if son % 2 == 0:
            juft_sonlar.append(son)
    return juft_sonlar


        