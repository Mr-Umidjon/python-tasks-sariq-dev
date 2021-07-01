# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:57:16 2021

@author: WINDOWS 10
"""

class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
        self.bosqich = 1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabsi. "
    
    def get_name(self):
        """Talabaning familiyasini qaytaradi."""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi."""
        return self.familiya
    
    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod."""
        self.bosqich = yangi_bosqich
    
    def update_bosqich(self):
        """Talabanining bosqichini bittaga ko'paytrish."""
        self.bosqich += 1
    
        
talaba1 = Talaba("Olim", 'Olimov')
talaba2 = Talaba("Olim", 'Omonov')
talaba3 = Talaba("Vali", 'Aliyev')


