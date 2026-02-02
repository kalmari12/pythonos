'''szam = 1

lista1 = []

while szam < 10:
    if szam % 2 == 0:
        print(f"{szam}") 
    szam += 1


szam = 10

while szam > 0:
    print(f"{szam}")
    szam -= 1

szam = 10

while szam > 0:
    if not szam % 2 == 0:
        print(f"{szam}")
    szam -= 1

szöveg = str(input("Kérem adjon meg egy szöveget: "))

print(f"A felhasználó által megadott szöveg: {szöveg}")


szam = int(input("Kérem adjon meg egy páros számot: "))

while szam % 2 == 0:
    print("Ez egy páros szám")
else:
    szam = int(input("A szám nem páros kérem adjon meg egy páros számot: "))'''

'''szam = 1

while szam % 2 !=  0:
    szam = int(input("Kérek egy páros számot: "))


import random

lista1 = []
lista2 = []

for x in range(20):
    lista1.append(random.randint(1, 12))

for x in lista1:
    if x % 3 == 0:
        lista2.append(x)



print(f"A hárommal osztható számok: {lista2}\n\n"
      f"Ennyi szám osztható hárommal a listábol: {len(lista2)}")
'''














