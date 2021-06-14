# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:56:40 2021

@author: WINDOWS 10
"""

def toliq_ism_yasa(ism, familiya):
    """To'liq ism qayatruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba1 = toliq_ism_yasa('olim', 'hakimov')
talaba2 = toliq_ism_yasa('ali', 'rajabov')

print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")



