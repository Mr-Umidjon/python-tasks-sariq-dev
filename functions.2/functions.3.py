# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:28:21 2021

@author: WINDOWS 10
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {"kompaniya":kompaniya,
            'model':model,
            'korobka':korobka,
            'rang':rangi,
            'yil':yili,
            'narh':narhi}
    return avto



avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info("GM", 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
avtolar = [avto1, avto2]
print("Online bozordagi mavjud avtomashinalar ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Noma\'lum'
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
       
    