# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:54:54 2021

@author: WINDOWS 10
"""

class Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxs xususiyatlar"""
        self.ism = ism.title()
        self.familiya = familiya.title()
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f" Passport: {self.passport}, {self.tyil}-yil."
        return info
    
    def get_age(self, yil):
        """SHaxsning yoshi"""
        return yil - self.tyil
    
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, malaka, tel):
        super().__init__(ism, familiya, passport, tyil)
        self.malaka = malaka
        self.tel = tel
        
    def get_malaka(self):
        return self.malaka
    
    def get_tel(self):
        return self.tel
    
    def get_info(self):
        info = f"Professor: {self.ism} {self.familiya}, malaka: {self.malaka} yil, tel: {self.tel} "
        return info
    
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, tel, email, jins, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)
        self.tel = tel
        self.email = email
        self.jins = jins
        
    def get_jins(self):
        return self.jins
    
    def get_email(self):
        return self.email
    
    def get_tel(self):
        return self.tel

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, tel, email, jins, passport, tyil, parol):
        super().__init__(ism, familiya, tel, email, jins, passport, tyil)
        self.parol = parol
        
    def ban_user(self):
        return "Foydalanuvchi bloklandi. "
    
    
pro = Professor('muhiddin', 'abduqodirov', 'ac1232443', 1956, 24, +998990193538)
user = Foydalanuvchi('umidjon', 'maxammadsoliyev', 990193538, 'talaba2020.tuit@gmail.com', 'erkak', 'ac21345', 2002)
