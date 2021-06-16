# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:28:59 2021

@author: WINDOWS 10
"""

from random import sample
from math import sqrt

x = list(range(0, 1001))
y = list(sample(x, k = 10))
print(y)

ildizlar = list(map(lambda n: sqrt(n), y))
print(ildizlar)

toq_sonlar = list(filter(lambda n: n % 2, y))
print(toq_sonlar)
