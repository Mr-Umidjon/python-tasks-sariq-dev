# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:24:59 2021

@author: WINDOWS 10
"""

import json

with open("students.json") as f:
    students1 = json.load(f)
    
for student in students1['student']:
  print(f"{student['name']} {student['lastname']}. "
        f"Faculty of {student['faculty']}")
    
  
    