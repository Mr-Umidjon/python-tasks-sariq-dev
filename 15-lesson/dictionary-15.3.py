# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:56:17 2021

@author: WINDOWS 10
"""

davlatlar = {
    "aqsh":"Washington",
    'malayziya':"Kuala-Lumpur",
    'italiya':'rim',
    'tojikiston':'dushanbe',
    "qirg'iziston":"bishkek",
    'rossiya':"maskva",
    'singapur':'sungapur',
    'qozoqiston':'nursulton',
    "o'zbekiston":"toshkent",
    'janubiy kareya':'seul'
    }
davlat = input("Qaysi davlatni potaxtini bilishni istaysiz ").lower()
poytaxt = davlatlar.get(davlat, "Bizda bu haqida ma'lumot yo'q")
print(poytaxt.capitalize())


