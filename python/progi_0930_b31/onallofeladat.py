import random

'''elemszam = int(input("kérek egy elemszamot: "))'''

szam1  = int(input("Kérek egy ekzdőértéket: "))

szam2 = int(input("kérek egy végértéket: "))

lista1oszto = []

listaszamokosztok = []

szam3ostok = []

szam4ostok = []

szam5ostok = []

szam6ostok = []

szam7ostok = []




for x in range (szam1, szam2):
    lista1oszto.append(random.randint(szam1, szam2))

print(f"Az első lista elemei a felhasznalo altal megadott kezdő-és végértékek alapján. {lista1oszto}")



szam3 = int(input("Kérek egy osztot: "))

szam4 = int(input("Kérek egy masodik osztot: "))

szam5 = int(input("Kérek egy harmadik osztot: "))

szam6 = int(input("Kérek egy negyedik osztot: "))

szam7 = int(input("Kérek egy otodik osztot: "))

for x in lista1oszto:
    if x % szam3 == 0:
        szam3ostok.append(x)
    if x % szam4 == 0:
        szam4ostok.append(x)
    if x % szam5 == 0:
        szam5ostok.append(x)
    if x % szam6 == 0:
        szam6ostok.append(x)
    if x % szam7 == 0:
        szam7ostok.append(x)

szam3ostok.sort(reverse=True)

szam4ostok.sort(reverse=True)

szam5ostok.sort(reverse=True)

szam6ostok.sort(reverse=True)

szam7ostok.sort(reverse=True)

print(f"A elso oszto: {szam3}, a vele osztahto szamok: {szam3ostok}\n\n"
      f"A masodik oszto: {szam4}, a vele osztahto szamok: {szam4ostok}\n\n"
      f"A harmadik oszto: {szam5}, a vele osztahto szamok: {szam5ostok}\n\n"
      f"A negyedik oszto: {szam6}, a vele osztahto szamok: {szam6ostok}\n\n"
      f"A otodik oszto: {szam7}, a vele osztahto szamok: {szam7ostok}")



