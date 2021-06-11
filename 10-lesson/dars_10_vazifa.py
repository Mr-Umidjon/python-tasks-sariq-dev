"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())
        
login = input("Logingizni kiriting ")
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foidalanuvchilar ro'yxatini ko'rasizmi? ")
else:
    print("Xush kelibsiz,", login.title())

print("Ikkita son kiriting ")
son1 = int(input("Birinchi sonni kiriting "))
son2 = int(input("Ikkinchi sonni kiriting "))
if son1 == son2:
    print("Sonlar teng ekan")
"""

son = int(input("Istalgan sonni kiriting ")) 
if son > 0:
    print("Musbat son")
else:
    print("Manfiy son")
    
    
    
