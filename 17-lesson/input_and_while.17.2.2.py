# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 09:16:31 2021

@author: WINDOWS 10
"""

# ishora
savol = "Yoshingiz nechida "
ishora = 1
while ishora:
    chipta = input(savol)
    if chipta.lower() == "quit" or chipta.lower() == "exit":
        ishora = 0
    else:
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