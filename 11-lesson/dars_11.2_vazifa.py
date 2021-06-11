# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:10:45 2021

@author: WINDOWS 10
"""

yosh = int(input("Yoshingiz nechida "))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
else:
    narh = 20000
print(f"Sizga kirish {narh} so'm ")