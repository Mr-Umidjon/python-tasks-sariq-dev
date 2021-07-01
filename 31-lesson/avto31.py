# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 12:58:43 2021

@author: WINDOWS 10
"""

from uuid import uuid4
class Avto:
    __num_avto = 0
    PI = 3.14159
    def __init__(self, make, model, rang, yil, narh, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
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
    
     