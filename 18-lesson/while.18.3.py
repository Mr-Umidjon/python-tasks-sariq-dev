# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:25:44 2021

@author: WINDOWS 10
"""

buyurtmalar = ['olma', 'non', 'uzum', 'qovun', 'osh']
mahsulotlar = {
    'olma':3000,
    'non':25000,
    'kabob':9000,
    'qovun':34000,
    'anjir':12000
    }

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} {mahsulotlar[buyurtma]} so'm ")
    else:
        print(f"Bizda {buyurtma} yo'q ")
        
        