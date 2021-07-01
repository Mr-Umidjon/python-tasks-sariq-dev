# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:42:48 2021

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
        self.fanlar = []
        
        
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
    
    def fanga_yozil(self, fan):
        self.fan = fan
        self.fanlar.append(fan)
        
    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz. ")
                
    
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


class Fan:
    def __init__(self, nom, yonalish, dars_soat):
        self.nom = nom
        self.dars_soat = dars_soat
        self.yonalish = yonalish
                
    def get_name(self):
        return self.nom
    
    def get_info(self):
        return f"{self.nom.title()} {self.yonalish} yo'nalishi, dars soatlari: {self.dars_soat} soat"
fan1 = Fan("Matematika", "aniq fanlar", 7)
fan2 = Fan("Fizika", "aniq fanlar", 3)
fan3 = Fan("Ona tili", "ijtimoiy gumanitar", 2)
         
talaba1_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")
talaba1 = Talaba('ali', 'akmalov', 'ac1234456', 2001, 123478, talaba1_manzil)
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)
        