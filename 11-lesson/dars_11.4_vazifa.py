# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:20:37 2021

@author: WINDOWS 10
"""

mahsulotlar = ['anor', 'olma', 'uzum', 'shaftoli', 'gilos', "o'rik", 'tarvuz', "qovun",\
               "handalak", 'kabob']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
            print(f"Do'konimizda {mahsulot} yo'q")