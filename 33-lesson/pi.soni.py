# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:24:45 2021

@author: WINDOWS 10
"""

import pickle

faylnomi = 'pi_million_digits.txt'
with open(faylnomi) as fayl:
    pi = fayl.read()
    
pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')   
print(pi)

if '15102002' in pi:
    print("bor")
    
pi = float(pi)

with open("PI", 'wb') as file:
    pickle.dump(pi, file)
    
    