# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:19:33 2021

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
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
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