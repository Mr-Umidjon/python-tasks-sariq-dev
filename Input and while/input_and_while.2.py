# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:45:49 2021

@author: WINDOWS 10
"""

# ishora
print("Kiritilgan sonni kivadratini qaytaruvchi dastur. ")
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print("Dastur tugadi. ")





