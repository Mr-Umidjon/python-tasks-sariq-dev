# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:20:48 2021

@author: WINDOWS 10
"""

kalit = input("Kalit so'zni kiriting: ").lower()
izohli_lugat = {'integer':'butun son', "float":"xaqiqiy son", 'string':"matn",\
                "if":"agar", 'else':'aks holda', 'list':"ro'yxat", "elif":"aks holda, agar",\
                'type':"o'zgaruvchi turini qaytaradi", 'dictionary':"lug'at",\
                'github':'dasturlash sayti'}
tarjima = izohli_lugat.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas ")
else:
    print(f"{kalit.title()} so'zi {tarjima.capitalize()} deb tarjima qilinadi")