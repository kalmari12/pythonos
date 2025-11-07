import random
import math

szam = int(5)

print(f"A szám sin: {math.sin(szam):.2f}")
print(f"A szám cos-: {math.cos(szam):.2f}")
print(f"A szám tangense: {math.tan(szam):.2f}")
print(f"A szám floora: {math.floor(12.56):.2f}") # az alatta levo elso egesz szamot irja ki vagyis leveszio a tizedes jegyet
print(f"A szám ceilingje: {math.ceil(15.67):.2f}") # a felette levo egesz szamot irja ki, vagyis leveszi a tizedes jegyet es felfele kerekit
print(f"A pi értéke: {math.pi}")
print(f"A szám hatvanyozas: {math.pow(4,2)}") # matematikai fuggvennyel valo  megoldas
print(f"{4**2}")
print(f"kerekitve {round(2.5352324523525423235, 2)}")

lista1 = []

for x in range(500):
    lista1.append(random.uniform(1.5, 234.8))

#print(f"{lista1}")

kereklista = []
nmemkereklista = []
hatvanyos = []
kisebblista = []
nagyobblista = []

for x in lista1:
    kereklista.append(round(x, 2))

print(kereklista)

for x in lista1:
    nmemkereklista.append(round(x, 2))


for x in  nmemkereklista:
    hatvanyos.append(f"{math.pow(x,2):.2f}")

print(hatvanyos)

for x in lista1:













