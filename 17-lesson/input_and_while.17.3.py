# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 09:38:21 2021

@author: WINDOWS 10
"""

# Xatolar ustida ishlash
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
     qiymat = input(savol)
     if qiymat.capitalize() == 'Exit':
         break
     else:
         qiymat = float(qiymat)
         if qiymat < 0:
             continue
         else:
             ildiz = float(qiymat)**(0.5)
             print(f"{qiymat} ning ildizi {ildiz} ga teng")
             
             