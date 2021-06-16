# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:02:55 2021

@author: WINDOWS 10
"""

def daraja(n):
    return lambda x : x ** n
kvadrat = daraja(2)
kub = daraja(3)

print(f"3 ning kvadrati {kvadrat(3)} ga, "
      f"kubi {kub(3)} ga teng.")
