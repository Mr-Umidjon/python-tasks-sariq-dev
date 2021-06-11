# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 08:51:24 2021

@author: WINDOWS 10
"""

ismlar = ['ali', 'vali', 'salim', 'gani', 'gopur']
for ism in ismlar:
    print("Salom", ism)
print("Kod", len(ismlar), "marta takrorlandi")

toq_sonlar = list(range(11, 100, 2))
for kub_toq in toq_sonlar:
    print(kub_toq**3)
    
kinolar = []
print("5 ta sevimli kino kiriting ")
for kino in range(5):
    kinolar.append(input(f'{kino+1}-kinoni kiriting '))
print(kinolar)

n = int(input("bugun nechta oadam bilan uchrashdingiz "))
insonlar = []

for inson in range(n):
    insonlar.append(input(f'{inson+1}-insonni kiriting '))
print(insonlar)