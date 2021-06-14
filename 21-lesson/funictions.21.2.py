# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:22:11 2021

@author: WINDOWS 10
"""


def katta_harf(matnlar):
    yangi_ismlar = []
    for matn in matnlar:
        yangi_ismlar.append(matn.title())
    return yangi_ismlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(yangi_ismlar)
print(ismlar)
      
