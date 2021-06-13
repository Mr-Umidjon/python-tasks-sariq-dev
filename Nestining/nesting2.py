# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:41:44 2021

@author: WINDOWS 10
"""

#Ro'yxat ichida lug'at
malibus = []
for n in range(10):
    new_car = {
        'model':"malibu",
        'rang':None,
        'yil':2021,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)
    
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
    
for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['korobka'] = 'maexanika'

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000
    
for malibu in malibus:
    print(malibu)
    
    
    
    


    