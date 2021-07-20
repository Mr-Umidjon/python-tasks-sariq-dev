# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 07:25:39 2021

@author: WINDOWS 10
"""

def get_full_name(ism, familiya, otasi = ''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()



