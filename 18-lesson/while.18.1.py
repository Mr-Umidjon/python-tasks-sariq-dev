# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:49:17 2021

@author: WINDOWS 10
"""

buyurtmalar = []
n=1
while True:
    savol = f"{n}-buyurtmangiz nima ? "
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    takrorlash = input("Boshqa buyurtmangiz ham bormi(ha/yo'q) ? ")
    n += 1
    if takrorlash != 'ha':
        break
    
  
    