# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:52:17 2021

@author: WINDOWS 10
"""
"""
davlatlar = ['AQSh', "Kanada", "Singapur", "Malayziya", "Qatar"]
print("Davlatlar soni",len(davlatlar), "ta")
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
"""

"""
juft_sonlar = list(range(120, 1200, 2))
jami = sum(juft_sonlar)
print(jami)

print(max(juft_sonlar) - min(juft_sonlar))

elementlar_soni = len(juft_sonlar)
print(elementlar_soni)

print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[260:280])
"""

taomlar = ["osh", "chuchvara", "kabob", "manti", 'somsa']
nonushta = taomlar[:]
nonushta.remove("osh")
nonushta.remove("manti")
del nonushta[1]

nonushta.append("sar yog'")
nonushta.insert(1, "qatiq")

print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)

































