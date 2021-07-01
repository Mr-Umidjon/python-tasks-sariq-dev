# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:57:09 2021

@author: WINDOWS 10
"""

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.__num_avto += 1
        
    def __str__(self):
        return f"Avto: {self.make} {self.model} "
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model} "
    
    def __eq__(self, y):
        return self.narh == y.narh
    
    
    def __lt__(self, y):
        return self.narh < y.narh
    
    def __le__(self, y):
        return self.narh <= y.narh   
    
class AvtoSalon :
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni "
    
    def __getitem__(self, index):
        return self.avtolar[index]
    
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat
        
    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
        
    def __add__(self, y):
        if isinstance(y, AvtoSalon):
            new_salon = AvtoSalon(f"{self.name} {y}")
            new_salon.avtolar = self.avtolar + y.avtolar
            return new_salon
        elif isinstance(y, Avto):
            self.add_avto(y)
    
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiritng")
        
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("AvtoLider")
        
avto1 = Avto("GM", 'Malibu', 'Qora', 2021, 40000, 100000)
avto2 = Avto("GM", 'Nexia', 'Qora', 2019, 50000, 800000)
avto3 = Avto("Toyota", 'Kia', 'Oq', 2020, 70000, 300000) 
avto4 = Avto("Mazda", 'X7', 'Qora', 2020, 40000, 500000)
avto5 = Avto("GM", 'Nexia2', 'Qora', 2017, 50000, 400000)
avto6 = Avto("Toyota", 'Kia3', 'Oq', 2021, 60000, 200000) 

salon1.add_avto(avto1, avto2, avto3)   
salon2(avto1, avto2)     
        
        
        
        
        