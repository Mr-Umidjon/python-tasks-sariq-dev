# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 08:48:53 2021

@author: WINDOWS 10
"""

# shart
savol = "Yoshingiz nechida "
chipta  = ''
while chipta.lower() != "quit" and chipta.lower() != "exit":
    chipta = input(savol)
    if chipta.lower() != "quit" and chipta.lower() != "exit":
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
    
 

       