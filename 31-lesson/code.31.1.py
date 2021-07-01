# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:42:41 2021

@author: WINDOWS 10
"""

from uuid import uuid4
class Avto:
    def __init__(self, make, model, rang, yil, narh, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        """Avtomilning yurgan km ni qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Avto km ni kamaytirib bo'lmaydi. ")
    
avto1 = Avto("GM", 'Malibu', 'Qora', 2021, 40000, 100000)   