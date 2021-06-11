# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:05:02 2021

@author: WINDOWS 10
"""

"""
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati" )
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
"""

kocha = input("Ko'changizni kiriting ").title()
mahalla = input("Mahallangizni kiriting ").title()
tuman = input("Tumaningizni kiriting ").title()
viloyat = input("Viloaytingizni kiriting ").title()
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati" )
print(kocha + " ko'chasi, \n" + mahalla + " mahallasi, \n" + tuman + " tumani, \n" + viloyat + " viloyati " )

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
