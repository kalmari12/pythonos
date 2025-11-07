import random

lista1 = []
lista2 = []

for x in range(5):
    lista1.append(random.randint(1,10))

for x in lista1:
    if x % 2 == 0:
        lista2.append(x)

print(f"A generált számok: {lista1}\n"
      f"A páros számok listája: {lista2}")

# 2.1 feladat

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal', 'alakul']
index = 0 

for betu in szavak:
    if betu[0] == "a" or "A":
        index = index + 1

print(f"A listában szereplő szavak közül ennyi kezdődik a vagy A val: {index}")

















