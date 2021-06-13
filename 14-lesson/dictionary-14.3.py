# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:59:29 2021

@author: WINDOWS 10
"""

izohli_lugat = {'integer':'butun son', "float":"xaqiqiy son", 'string':"matn",\
                "if":"agar", 'else':'aks holda', 'list':"ro'yxat", "elif":"aks holda, agar",\
                'type':"o'zgaruvchi turini qaytaradi", 'dictionary':"lug'at",\
                'github':'dasturlash sayti'}
kalit = input("Kalit so'zni kiriting: ")
tarjima = izohli_lugat.get(kalit, 'Bunday so\'z mavjud emas ').capitalize()
print(tarjima)





