# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:12:00 2021

@author: WINDOWS 10
"""

def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
    """To'liq ism qayatruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"  
    return toliq_ism.title()

talaba1 = toliq_ism_yasa('olim', 'hakimov', 'akbarovich')
talaba2 = toliq_ism_yasa('ali', 'rajabov')

print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")
