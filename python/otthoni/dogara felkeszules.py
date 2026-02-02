import random

lista1 = []
szamolo = 0

for x in range(50):
    lista1.append(random.randint(1,100))

lista1.sort()
print(f"{lista1}")

print(f"A lista legkisebb eleme: {max(lista1)}")
print(f"A lista legnagyobb eleme: {min(lista1)}")


adjameg = int(input(f"Kérem adjon meg egy szamot 1 és 100 kozott: "))

if adjameg in lista1:
    print(f"A megadott szam megtalalhato a listaban")
else:
    print(f"A megadott szam nincs a listaban")

for x in lista1:
    if x == adjameg:
        szamolo += 1

if adjameg in lista1:
    print(f"A megadott szam ennyiszer volt a listaban: {szamolo}")
else:
    print(f"A megadott szam nem talalhato a listaban")

print(f"Ennyi elem van a listában: {len(lista1)}")

print(f"A lista elso 10 eleme: {lista1[:10]}")

lista2 = []
for k in lista1:
    if k % 2 == 0:
        lista2.append(k)
print(f"A listaban levo paros elemek: {lista2}")

index = 0
for x in lista1:
    print(f"{index}. elem: {x}")
    index += 1

if lista1[15] != None:
    print(f"A listanak nincs 15. elem")
else:
    print(f"A lsitának a 15. eleme: {lista1[15]}")

if lista1[5] != None:
    print(f"A listanak nincs 5. elem")
else:
    print(f"A lsitának a 5. eleme: {lista1[1]}")


if lista1[5:15] == None:
    print(f"A lista nem tartalmaz 5 és 15 kozott elemeket")
else:
    print(f"A lista elemei 5 és 15 kozott: {lista1[5:15]}")

lista1.pop()

lista1.insert(3, 10)

lista1.reverse()

lista1masolat = lista1.copy()

szum = sum(lista1)
atlag = sum(lista1)/len(lista1)

print(f"A lista elemeinek osszege: {szum}")
print(f"A lista eleminek atlaga: {atlag}")

list3 = []

for x in lista1:
    if x > 100:
        list3.append(x)

print(f"A listaban levo elemek amik nagyobbak mint 100 {list3}")

lista1.remove(lista1[7])

adjameg2 = int(input("Kérem adjon meg egy szamot: "))

for x in lista1:
    if x == adjameg2:
        lista1.remove(x)

print(f"A lista elso 5 eleme: {lista1[:5]}")
print(f"A listaban levo elemek 10-tol 20 ig: {lista1[10:20]}")

index = 0
lista4 = []

for x in lista1:
    if index % 2 == 0:
        lista4.append(x)
    index += 1

print(lista4)

lista5 = [4,5,6,7]

lista5.append(lista1)
print(lista5)


strlista = ["ez", "egy", "szöveges", "lista"]