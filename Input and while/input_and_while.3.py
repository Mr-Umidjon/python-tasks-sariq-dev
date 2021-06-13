# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:55:42 2021

@author: WINDOWS 10
"""

# break while
print("Kiritilgan sonni kivadratini qaytaruvchi dastur. ")
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)
print("Dastur tugadi. ")





