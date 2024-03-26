import random 

nombre1 = random.randint(1, 50)
nombre2 = random.randint(1, 50)
nombre3 = random.randint(1, 50)
nombre4 = random.randint(1, 50)
nombre5 = random.randint(1, 50)
numeroChance1 = random.randint(1, 12)
numeroChance2 = random.randint(1, 12)

while nombre1 == nombre2 or nombre1 == nombre3 or nombre1 == nombre4 or nombre1 == nombre5 or nombre2 == nombre3 or nombre2 == nombre4 or nombre2 == nombre5 or nombre3 == nombre4 or nombre3 == nombre5 or nombre4 == nombre5 or nombre5 == nombre1:
    nombre1 = random.randint(1, 50)
    nombre2 = random.randint(1, 50)
    nombre3 = random.randint(1, 50)
    nombre4 = random.randint(1, 50)
    nombre5 = random.randint(1, 50)


print("nombre1", nombre1, "nombre2", nombre2, "nombre3", nombre3, "nombre4", nombre4, "nombre5", nombre5,"numeroChance1", numeroChance1 ,"numeroChance2", numeroChance2)