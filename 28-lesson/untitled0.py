# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:11:53 2021

@author: WINDOWS 10
"""

class Talaba():
    def __init__(self, ism, familiya, tyil):
        self.name = ism.title()
        self.surename = familiya.upper()
        self.data = tyil
    
    def get_name(self):
        return self.name
    
    def get_age(self, yil):
        return yil - self.data

    def get_lastname(self):
        return self.surename
    
    def tanishtir(self):
        return f"Ismim {self.name} {self.surename}, tug'ilgan yilim {self.data}"
        
talaba = Talaba('olim', 'valiyev', 2000)
talaba1 = Talaba('kamol', 'aliyev', 1990)
talaba2 = Talaba("ali", 'valiyev', 2002)     

