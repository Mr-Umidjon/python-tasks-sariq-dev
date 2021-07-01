# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:24:50 2021

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
    
    def get_fullname(self):
        """Talabaning to'liq ismini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def get_info(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
        


class Fan():
    """Fan nomli klass"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fang yozilgan talabalar haqida ma'lumot."""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni haqida ma'lumot."""
        return self.talabalar_soni
    
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
    
  
    
  
matematika = Fan("Oliy matematika")
talaba1 = Talaba("Olim", 'Olimov', 2000)
talaba2 = Talaba("Olim", 'Omonov', 2007)
talaba3 = Talaba("Vali", 'Aliyev', 2005)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
    