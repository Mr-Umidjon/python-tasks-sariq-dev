# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:43:24 2021

@author: WINDOWS 10
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan', 'botir']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

