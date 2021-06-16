# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:24:03 2021

@author: WINDOWS 10
"""

a = [4, 5, 6]
b = [7, 8, 9]

a_plus_b = list(map(lambda x, y: x + y, a, b))
print(a_plus_b)

ismlar = ['hasan', 'husan', 'olim', 'ali', 'vali']
print(list(map(lambda matn: matn.upper(), ismlar)))