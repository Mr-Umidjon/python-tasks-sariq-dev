# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:24:17 2021

@author: WINDOWS 10
"""

# input()
"""
ism = input("Ismingiz nima ? ")
savol = f"Salom {ism.title()}. Yoshingiz nechida ? "
yosh = input(savol)
height = input("Bo'yingiz nechi metr ? ")
height = float(height)
"""

# while()
"""
son = 1
while son <= 5:
    print(son, end = ' ')
    son = son + 1
print("Dastur tugadi ")
"""

# while and input
print("Kiritilgan sonni kivadratini qaytaruvchi dastur. ")
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ' '
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print("Dastur tugadi. ")




