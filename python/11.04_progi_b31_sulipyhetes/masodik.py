import random
# Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!

lista1 = []
talalat = False
index = 0

for x in range(5):
    lista1.append(random.randint(1,7))

szam1 = int(input("Kérek egy szamot: "))

"""for x in lista1:
    if szam1 == x:
        print(f"A megadott szám benne van a listában, a lista elemei: {lista1}")
    else:
        print(f"A szám nincs benne a listában :(, a lista elemi: {lista1})")"""

while index < len(lista1) and not talalat:
    if lista1[index] == szam1:
        talalat = True
    index = index + 1

if talalat:
    print("A listaban van a szam")
else:
    print("a listaban nincs ilyen szam")

