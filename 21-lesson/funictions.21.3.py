# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:47:27 2021

@author: WINDOWS 10
"""

talabalar = ['ali', 'vali', 'hasan', 'husan', 'botir']
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar

baholar = bahola(talabalar)   
print(baholar)
print(talabalar)   

