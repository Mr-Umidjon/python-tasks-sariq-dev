# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:09:05 2021

@author: WINDOWS 10
"""

import json

data = {
        "Model": "Malibu",
        "Rang": "Qora",
        "Yil": "2021",
        "Narh": 40000
        }

data_json = json.dumps(data, indent=4)


talaba_json = """{"ism": "Hasan", "familiya": "Husanov", "tyil": 2001}"""

talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")

with open("data.json", 'w') as f:
    json.dump(data, f)
    
with open("talba.json", 'w') as f:
    json.dump(talaba, f)