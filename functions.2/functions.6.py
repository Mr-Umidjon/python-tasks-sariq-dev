# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:09:10 2021

@author: WINDOWS 10
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {"kompaniya":kompaniya,
            'model':model,
            'korobka':korobka,
            'rang':rangi,
            'yil':yili,
            'narh':narhi}
    return avto

print("Sayitimizdagi avtolar ro'yxatini shakillantiramiz ")
avtolar = []
while True:
    print("\n Quyidagi ma'lumotlarni kiritng ", end = ' ')
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")  
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana avto qo'shasizmi (ha/yo'q) ")
    if javob != "ha":
        break

print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, \
          {avto['korobka']} korobka. Narhi: {narh}")
          
          
          
          
          
          