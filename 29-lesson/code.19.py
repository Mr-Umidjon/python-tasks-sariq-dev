# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:53:51 2021

@author: WINDOWS 10
"""

class Talaba():
    def __init__(self, ism, familiya, tyil):
        self.name = ism.title()
        self.surename = familiya.upper()
        self.data = tyil
        self.kurs = 1
    
    def get_info(self):
        return f"{self.name} {self.surename}, {self.kurs}-bosqich talabasi. "
    
    def get_name(self):
        "Talabaning ismini qaytaradi."
        return self.name
    
    def get_age(self, yil):
        "Talabaning yoshini qaytaradi. "
        return yil - self.data
    
    def get_fullname(self):
        """Talabaning to'liq ismini chiqaradi."""
        return f"{self.name} {self.surename}"

    def get_lastname(self):
        "Talabaning familiyasini qaytaradi. "
        return self.surename
    
    def set_kurs(self, new_kurs):
        """Talabaning kursini yangilovchi metod. """
        self.kurs = new_kurs
        
    def update_kurs(self):
        """Talabaning bosqichini 1 taga ko'paytiradi. """
        self.kurs += 1
        
     

class Fan():
    def __init__(self, nomi):
        self.nomi = nomi.title()
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self, talaba):
        """Fanga talabalar qo'shish. """
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        """Fan nomi."""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot. """
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yoziligan talabalar soni. """
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]      



talaba = Talaba('olim', 'valiyev', 2000)
talaba1 = Talaba('kamol', 'aliyev', 1990)
talaba2 = Talaba("ali", 'valiyev', 2002)  
matematika = Fan('Oliy matematika')  
matematika.add_student(talaba)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
  
    
  