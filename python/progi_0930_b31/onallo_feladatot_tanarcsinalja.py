import random

szamlista = []

elemszam = int(input("hány elemet sorsoljak: "))
kezdoertek = int(input("Kérek egy kezdoerteket: "))
vegertek = int(input("kerek egy veg óerteket: "))

for x in range(elemszam):
    szamlista.append(random.randint(kezdoertek, vegertek))

oszto1 = int(input("kérek egy osztot:"))

oszto2 = int(input("kérek egy masik osztot:"))

oszto3 = int(input("kérek egy masik osztot:"))

oszto4 = int(input("kérek egy masik osztot:"))

oszto5 = int(input("kérek egy masik osztot:"))



lsita1 = []
lsita2 = []
lsita3 = []
lsita4 = []
lsita5 = []

for x in szamlista:
    if x % oszto1 == 0:
        lsita1.append(x)
    if x % oszto2 == 0:
        lsita2.append(x)
    if x % oszto3 == 0:
        lsita3.append(x)
    if x % oszto4 == 0:
        lsita4.append(x)
    if x % oszto5 == 0:
        lsita5.append(x)


lsita1.sort(reverse=True)
lsita2.sort(reverse=True)
lsita3.sort(reverse=True)
lsita4.sort(reverse=True)
lsita5.sort(reverse=True)

