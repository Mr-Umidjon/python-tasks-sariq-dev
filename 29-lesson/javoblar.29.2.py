# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:16:13 2021

@author: WINDOWS 10
"""

class Avto():
    def __init__(self, ishlab_chiqaruvchi, model, rang, korobka, narh):
        self.ishlab_chiqaruvchi = ishlab_chiqaruvchi.upper()
        self.model = model.title()
        self.rang = rang.title()
        self.narh = narh
        self.korobka = korobka
        self.kilometr = 0
        
class Avtosalon():
    def __init__(self, salon, manzil, sotuvdagi_avtolar):
        self.salon = salon.capitalize()
        self.manzil = manzil.capitalize()
        self.sotuvdagi_avtolar = sotuvdagi_avtolar
  
    def add_avto(self, avto):
        self.sotuvdagi_avtolar.append(avto)
        
    def get_info(self):
        return [avto for avto in self.sotuvdagi_avtolar]
avto = Avto("gm", "nexia 3", 'oq', 'avtomat', 7000)
avtolar = Avtosalon("andijon", 'toshkent', ["nexia"])      
avtolar.add_avto('malibu')