import random
import math


lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

fszam = int(input("Kérek egy számot:"))

for x in range(200):
    lista1.append(random.randint(1, 1000))

lista1.sort()

print(f"listában lévő számok összege: {sum(lista1)}\n"
      f"A felhasználó által megadott szám: {fszam} \n")

for  x in lista1:
    if x % 2 == 0:
        lista2.append(x)
    if not x % 2 == 0:
        lista4.append(x)
    if x % 3 == 0:
        lista3.append(x)
    if x % fszam == 0:
        lista5.append(x)

atlag = sum(lista1) / len(lista1)

print(f"A listában lévő számok: {lista1}\n\n"
      f"A listában lévő páros számok: {lista2}\n\n"
      f"A listában lévő páratlan számok: {lista4}\n\n"
      f"A listában lévő hárommal osztható számok: {lista3}\n\n"
      f"A listában lévő páros elemek összege: {sum(lista2)}\n\n"
      f"A listában lévő hárommal osztható elemek összege: {sum(lista3)}\n\n"
      f"A legnagyobb szám a listában: {max(lista1)}\n\n"
      f"A legkisebb szám a listában: {min(lista1)}\n\n"
      f"A számok átlaga: {atlag}\n\n"
      f"A felhasználó által megadott számmal osztahtó elemek: {lista5}\n\n"
      f"Az alaplistának az első elem: {lista1[0]}\n\n"
      f"Az alaplistának az utolsó eleme: {lista1[-1]}\n\n"
      f"Az alaplista első elemének illetve a felhasználó által megadott szám hányadosa: {lista1[0] / fszam}")








