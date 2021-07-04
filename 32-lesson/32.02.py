# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:04:13 2021

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
    
    def __repr__(self):
        return f"Shaxs: {self.get_info()}"
    
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
    
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        return bosqich
        
    def __repr__(self):
        return f"Talaba: {self.get_info()}"
    
    def __lt__(self, y):
        return self.bosqich < y.bosqich
    
    def __le__(self, y):
        return self.bosqich <= y.bosqich
    
    def __eq__(self, y):
        return self.bosqich == y.bosqich
    
class Fan:
    def __init__(self, name):
        self.name = name
        self.fan_yozilgan = []
        
    def __repr__(self):
        return f"{self.name}"
        
    def add_student(self, *qiymat):
        for talaba in qiymat:
            if isinstance(talaba, Talaba):
                self.fan_yozilgan.append(talaba)
            
    def __getitem__(self, index):
        return self.fan_yozilgan[index]
    
    def __setitem__(self, index, qiymat):
        self.fan_yozilgan[index] = qiymat
        
    def __len__(self):
        return len(self.fan_yozilgan)
    
    def __add__(self, talaba):
        if isinstance(talaba, Talaba):
            self.add_student(talaba)
            
    def __sub__(self, talaba):
        if isinstance(talaba, Talaba):
            self.fan_yozilgan.remove(talaba)
            
    def __call__(self, *qiymat):
        if qiymat:
            for talaba in qiymat:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.fan_yozilgan]
            
    
    
    
        
fan1 = Fan("Matematika")  
  
talaba0 = Talaba("Umidbek", "Maxammadsoliyev", "AC123234", 2002, 3252365, "Andijon")
talaba1 = Talaba("Umidjon", "Toshev", "AC675498", 2003, 897654, "Buxoro")
talaba2 = Talaba("Sardor", "Ibodov", 987654, 2003, 76543, "Qarshi")
talaba3 = Talaba("Umidjon", "Toshev", 89765098, 2003, 76658, "Shofirkon")
shaxs0 = Shaxs("Ali", "Valiyev", "AA98767", 2001)
fan1.add_student(talaba1, talaba0, talaba2, talaba3)

