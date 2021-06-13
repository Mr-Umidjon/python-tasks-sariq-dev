# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 08:18:59 2021

@author: WINDOWS 10
"""

savol = "Sevgan kitoblaringizni kiriting "
savol += "(barch kitoblarni kiritib bo'lganizdan keyin 'stop' deb yozing) "
while True:
    kitob = input(savol)
    if kitob.lower() == 'stop':
        break
print("Raxmat !")
        