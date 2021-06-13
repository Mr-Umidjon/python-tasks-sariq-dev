# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:37:08 2021

@author: WINDOWS 10
"""

talabalar = ['hasan', 'ali', 'vali', 'husan', 'karim', 'olim', 'botir']
baholangan_talabalar = {}

while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = int(baho)
    
    
    
       
    