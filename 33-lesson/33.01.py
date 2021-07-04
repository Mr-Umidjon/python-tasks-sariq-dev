# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:27:14 2021

@author: WINDOWS 10
"""

faylnomi = "new_file.txt"
ism = "olim karimov"
tyil = 2003
with open(faylnomi, 'w') as fayl:
    fayl.write(ism + '\n')
    fayl.write(str(tyil) + '\n')
    
