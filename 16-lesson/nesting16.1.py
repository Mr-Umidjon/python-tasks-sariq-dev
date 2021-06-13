# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:19:49 2021

@author: WINDOWS 10
"""

buxoriy = {
    'ism':"Abu Abdulloh Muhammad ibn Ismoil",
    'tyil':810,
    'tjoy':'buxoro',
    'vyil':870
    }
qodiriy = {
    'ism':"Abdulla Qodiriy",
    'tyil':1894,
    'tjoy':'toshkent',
    'vyil':1938
    }

vohidov = {
    'ism':"Erkin Vohidov",
    'tyil':1936,
    'tjoy':"fargona",
    'vyil':2016
    }
navoiy = {
    'ism':"Alisher Navoiy",
    'tyil':1441,
    'tjoy':'xirot',
    'vyil':1501
    }
mashxurlar = [buxoriy, qodiriy, vohidov, navoiy]
for mashxur in mashxurlar:
    print(f"\n{mashxur['ism']} {mashxur['tyil']}-yilda\
 {mashxur['tjoy'].title()}da tavallud topgan.\
 {mashxur['vyil']-mashxur['tyil']} umr ko'rgan.")
 
 
 