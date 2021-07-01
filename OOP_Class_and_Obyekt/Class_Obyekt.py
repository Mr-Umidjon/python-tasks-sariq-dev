# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:09:08 2021

@author: WINDOWS 10
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
        
talaba1 = Talaba("Olim", 'Olimov', 2000)
talaba2 = Talaba("Olim", 'Omonov', 2007)
talaba3 = Talaba("Vali", 'Aliyev', 2005)

