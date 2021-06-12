# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:41:47 2021

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
print("Dunyo davlatlari : ")
for d in sorted(davlatlar):
    print(d.upper())
print("\n")
    
print("Davlatlar poytaxtlari :")
for p in sorted(davlatlar.values()):
    print(p.title())
    
