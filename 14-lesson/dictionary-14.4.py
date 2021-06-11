# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:12:11 2021

@author: WINDOWS 10
"""
kalit = input("Kalit so'zni kiriting: ")
izohli_lugat = {'integer':'butun son', "float":"xaqiqiy son", 'string':"matn",\
                "if":"agar", 'else':'aks holda', 'list':"ro'yxat", "elif":"aks holda, agar",\
                'type':"o'zgaruvchi turini qaytaradi", 'dictionary':"lug'at",\
                'github':'dasturlash sayti'}
if kalit.lower() in izohli_lugat:
    print(f"{kalit.title()}, {izohli_lugat[kalit].capitalize()}")
else:
    print("Bunday so'z mavjud emas ")