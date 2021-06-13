# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:48:05 2021

@author: WINDOWS 10
"""

def mijoz_info(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email = '', tel_raqami = None):
    """Mijoz haqidagi ma'lumotlarni lug'atga kiritadi"""
    mijoz = {
        'ism':ismi,
        'familiya':familiyasi,
        "tugilgan_yil":tugilgan_yili,
        'tugilgan_joyi':tugilgan_joyi,
        'email':email,
        'tel_raqam':tel_raqami
        }
    return mijoz
print("Mijoz haqidagi ma'lumotlarni kiriting. ")
mijozlar = []
while True:
    ismi = input("Ismingiz: ")
    familiyasi = input("Familyangiz : ")
    tugilgan_yili = int(input("Tug'ilgan yilingiz: "))
    tugilgan_joyi = input("Tug'ilgan joyingiz: ")
    email = input("Elektron manzilingiz: ")
    tel_raqami = input("Telefon raqamingiz: ")
    mijozlar.append(mijoz_info(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email, tel_raqami))
    javob = input("Davom etasizmi ? (yes/no)")
    if javob != 'yes':
        break
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
          f"{2021 - mijoz['tugilgan_yil']} yoshda, telefoni: {mijoz['tel_raqam']}")
    
    
    
    
    
    