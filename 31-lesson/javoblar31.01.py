# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:13:39 2021

@author: WINDOWS 10
"""

class Shaxs:
    """Shaxs haqida ma'lumot"""
    odamlar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxs xususiyatlar"""
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        Shaxs.odamlar_soni += 1
     
    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni
    
        
    def get_passport(self):
        return self.__passport
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" Passport: {self.get_passport()}, {self.tyil}-yil ."
        return info
    
    def get_age(self, yil):
        """SHaxsning yoshi"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        Talaba.talabalar_soni += 1
   
    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

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
inson0 = Shaxs("Umidbek", "Maxammadsoliyev", 65245465, 2002) 
inson1 = Shaxs("Odiljon", "Maxammadsoliyev", 9087654, 2004)
inson2 = Shaxs("Muhammadziyo", "Avazbekov", 897890909, 2017)


talaba0 = Talaba("Sardor", "Ibodov", 987654, 2003, 76543, "Qarshi")
talaba1 = Talaba("Umidjon", "Toshev", 89765098, 2003, 76658, "Shofirkon")
                