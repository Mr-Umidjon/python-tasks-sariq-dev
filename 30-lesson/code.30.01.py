# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:26:37 2021

@author: WINDOWS 10
"""

class Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxs xususiyatlar"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" Passport: {self.passport}, {self.tyil}."
        return info
    
    def get_age(self, yil):
        """SHaxsning yoshi"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" {self.bosqich}-bosqich. ID: {self.get_id()}."
        return info
    
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish """
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

talaba1_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")
talaba1 = Talaba('ali', 'akmalov', 'ac1234456', 2001, 123478, talaba1_manzil)
        
    
    
    
 