# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:11:52 2021

@author: WINDOWS 10
"""

from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))
#print(ildizlar)


#def daraja2(x):
#    """Berilgan sonni kivadrtatini qaytaruvchi funksiya"""
#    return x * x

#print(list(map(daraja2, sonlar)))

#kvadratlar = list(map(lambda x : x * x, sonlar))
#print(kvadratlar)

kvadratlar = []
for son in sonlar:
    kvadratlar.append(son * son)
    
print(kvadratlar)

