# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:15:32 2021

@author: WINDOWS 10
"""

import pickle

with open("pi_million_digits.txt") as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace("\n", '')
pi = pi.replace(' ','')
bdate = '15102002'

print(bdate in pi)

pi = float(pi)


with open("pi_float", 'wb') as file:
    pickle.dump(pi, file)
    