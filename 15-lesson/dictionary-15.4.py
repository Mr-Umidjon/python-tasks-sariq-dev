# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:30:08 2021

@author: WINDOWS 10
"""

menu = {"osh":14000, 'bishteks':12000, 'dimlama':17000, 'non':4000,\
        'makaron':11000, 'shavli':13000, "lag'mon":15000, "choy":5000,\
            'shashlik':10000, 'somsa':6000, 'tabaka':15000}
buyurtmalar = []
print("3 ta taom buyurtma qiling ")
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")

 



   