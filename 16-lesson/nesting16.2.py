# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:46:25 2021

@author: WINDOWS 10
"""

buxoriy = {
    'ism':"Abu Abdulloh Muhammad ibn Ismoil",
    'tyil':810,
    'tjoy':'buxoro',
    'vyil':870,
    'asarlar':["Al-jome' as-sahih", "Al-adab al-mufrad", "Al-tarix al-kabir", "Al-tarix al-sag'ir"]
    }
qodiriy = {
    'ism':"Abdulla Qodiriy",
    'tyil':1894,
    'tjoy':'toshkent',
    'vyil':1938,
    'asarlar':["O'tkan kunlar", "Mehrobdan chayon", "Obid ketmon"]
    }

vohidov = {
    'ism':"Erkin Vohidov",
    'tyil':1936,
    'tjoy':"fargona",
    'vyil':2016,
    'asarlar':['Tong nafasi', "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
    }
navoiy = {
    'ism':"Alisher Navoiy",
    'tyil':1441,
    'tjoy':'xirot',
    'vyil':1501,
    'asarlar':["Xamsa", "Lison ut-Tayr", 'Mahbub Al-Qulub', 'Munojat']
    
    }
mashxurlar = [buxoriy, qodiriy, vohidov, navoiy]
for mashxur in mashxurlar:
    print(f"\n{mashxur['ism']}ning mashxur asarlari: ")
    for asar in mashxur['asarlar']:
        print(asar)







