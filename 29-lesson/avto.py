# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:14:37 2021

@author: WINDOWS 10
"""

class Avto:
    
    def __init__(self, model, rang, korobka, narh, ) :
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0
        
    def get_info(self):
        """Avto haqida to'liq ma'lumotni qaytaradi."""
        return f"{self.rang.title()} {self.model}. {self.korobka.title()} korobka, narhi: {self.narh} $, kilometri: {self.kilometr}"
    
    def update_km(self, km):
        """Avtoning km ni yangilaydi."""
        self.kilometr += km
        return self.kilometr        
avto = Avto("nexia", 'qora', 'avtomat', 23000)      