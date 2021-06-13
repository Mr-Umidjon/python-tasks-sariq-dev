# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:57:59 2021

@author: WINDOWS 10
"""

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':"oliy",
           'tillar':['python', 'c++']
        },
    'vali':{'familiya':'aliyev',
           'tyil':2001,
           'malumot':"o'rta maxsus",
           'tillar':['html', 'css', 'js']
        },
    'hasan':{'familiya':'husanov',
           'tyil':1999,
           'malumot':"maxsus",
           'tillar':['python', 'php']
        }}
for ism, info in hamkasblar.items():
    print(f'\n{ism.title()} {info["familiya"].title()}, '
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. "
          f"Quyidagi dasturlash tillarini biladi ")
    for til in  info['tillar']:
        print(til.upper())
        
        
        
        
        
        
        
        
        
        