# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:20:28 2021

@author: WINDOWS 10
"""


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()      
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar) 
print(ismlar)
      