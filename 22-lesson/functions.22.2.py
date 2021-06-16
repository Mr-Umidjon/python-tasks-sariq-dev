# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:42:58 2021

@author: WINDOWS 10
"""

def talaba_info(ism, familiya, **malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba0 = talaba_info('umidbek', 'maxammadsoliyev', yosh = 18)
talaba1 = talaba_info('sardor', 'ibodov', yosh = 18, fakultet = "KIF")