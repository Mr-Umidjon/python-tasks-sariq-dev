# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:00:26 2021

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
        
    def get_info(self):
        """Avto haqida ma'lumot"""
        return f"{self.rang} {self.model}, ishlab chiqaruvchi: {self.ishlab_chiqaruvchi},\
            korobka: {self.korobka}, km: {self.kilometr}, narh: {self.narh} $"
            
    def update_km(self, km):
        self.kilometr += km
        
    def set_narh(self, yangi_narh):
        self.narh = yangi_narh
        
avto = Avto("gm", "nexia 3", 'oq', 'avtomat', 7000)

