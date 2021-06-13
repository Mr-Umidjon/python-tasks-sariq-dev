# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 08:25:09 2021

@author: WINDOWS 10
"""

# break
savol = "Yoshingiz nechida "

while True:
    chipta = input(savol)
    if chipta.lower() == "quit" or chipta.lower() == "exit":
        break
    yosh = int(chipta)
    
    if yosh < 7:
        narh = 2000
    elif (yosh > 7 and yosh < 18):
        narh = 3000
    elif (yosh >= 18 and yosh <= 65):
        narh = 10000
    else:
        narh = 0
    if narh == 0:
        print("Sizga kirish bepul ")
    else:
        print(f"Sizga kirish {narh} so'm ")

