# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:53:54 2021

@author: WINDOWS 10
"""

class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        
    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.name}, email: {self.email}"
    
user1 = User("Umidjon", "Umidbek", "talaba2020.tuit@gmail.com")
user2 = User("Odiljon", "Kichkintoy", "OdiljonBoy@gmail.com") 

