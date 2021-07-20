# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 08:11:19 2021

@author: WINDOWS 10
"""

def tubSonmi(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True