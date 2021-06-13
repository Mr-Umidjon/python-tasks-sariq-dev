# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:08:52 2021

@author: WINDOWS 10
"""

# while ro'yxatlar
print("Yaqin do'stlaringiz ro'yxatini tuzamiz ")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingizni ismini kiriting "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi ? (ha/yo'q) ")
    n += 1
    if takrorlash != 'ha':
        break
print("Do'stlaringiz ro'yxati ")    
for ism in ismlar:
    print(ism.title())
    
    
    