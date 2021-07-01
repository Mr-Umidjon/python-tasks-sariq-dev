# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:58:59 2021

@author: WINDOWS 10
"""
class User():
    def __init__(self, ism , familiya, foydalanuvchi_ismi, email):
        self.name = ism.title()
        self.surename = familiya.title()
        self.username = foydalanuvchi_ismi
        self.email = email
    
    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.name} {self.surename}, email: {self.email}"
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_surename(self):
        return self.surename
    
user = User('umidjon', 'maxammadsoliyev',"mr_umidjon", 'talaba2020@gmail.com')
user1 = User('odiljon', 'maxammadsoliyev', 'odiljonboy', 'telefona11@gmail.com')