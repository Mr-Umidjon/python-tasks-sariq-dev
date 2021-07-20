# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:22:22 2021

@author: WINDOWS 10
"""

import unittest
from untitled49 import Shaxs, Talaba

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        self.ism = "Umidbek"
        self.familiya = "Maxammadsoliyev"
        self.passport = "AC1234556"
        self.tyil = 2002
        self.shaxs1 = Shaxs(ism = self.ism, familiya = self.familiya, passport = self.passport, tyil = self.tyil)
        
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        
    def test_age(self):
        age = self.shaxs1.get_age(2021)
        self.assertEqual(19, age)
        
    def test_info(self):
        info = self.shaxs1.get_info()
        info1 = "Umidbek Maxammadsoliyev. Passport: AC1234556, 2002."
        self.assertEqual(info, info1)

class TalabaTest(unittest.TestCase):
    def setUp(self):
        self.ism = "Umidbek"
        self.familiya = "Maxammadsoliyev"
        self.passport = "AC1234556"
        self.tyil = 2002
        self.id = 123254
        self.talaba = Talaba(ism = self.ism, familiya = self.familiya, passport = self.passport, tyil = self.tyil, idraqam = self.id)
    
    def test_id(self):
        idraqam1 = self.talaba.idraqam
        self.assertEqual(idraqam1, 123254)
        
    def test_bosqich(self):
        bosqich = self.talaba.bosqich
        self.assertEqual(bosqich, 1)
        
        
unittest.main()