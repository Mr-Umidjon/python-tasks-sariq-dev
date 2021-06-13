# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:57:50 2021

@author: WINDOWS 10
"""

e_bozor = {}
while True:
    savol = "Mahsulot nomini kiriting "
    mahsulot = input(savol)
    savol = f"{mahsulot.title()} narhini kiriting "
    narh = int(input(savol))
    e_bozor[mahsulot] = narh
    takrorlash = input("Yana mahsulot qo'shasizmi (ha/yo'q) ")
    
    if takrorlash != 'ha':
        break
    
    