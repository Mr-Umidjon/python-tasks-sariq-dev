# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:18 2021

@author: WINDOWS 10
"""
mahsulotlar = ['anor', 'olma', 'uzum', 'shaftoli', 'gilos', "o'rik", 'tarvuz', "qovun",\
               "handalak", 'kabob']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if not mavjud_emas:
    print("Siz so'ragan barcha mahsulot do'konimizda bor ")
else:
    print("Do'konimizda quydagi mahsulotlar yo'q ")
    for a in mavjud_emas:
        print(a)