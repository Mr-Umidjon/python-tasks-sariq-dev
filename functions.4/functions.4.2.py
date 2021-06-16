# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:28:10 2021

@author: WINDOWS 10
"""

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('GM', 'Malibu', rang = 'Qora', korobka = 'Avtomat', yil = 2018)
avto2 = avto_info("GM", 'Gentra', rang = 'Oq', korobka = 'Mexanika', yil = 2016, narh = 15000)