# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:30:26 2021

@author: WINDOWS 10
"""


def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title() 
    return matnlar
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(yangi_ismlar)
print(ismlar)


