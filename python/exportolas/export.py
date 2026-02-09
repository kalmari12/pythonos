import random

szamlsita = []

for x in range(500):
    szamlsita.append(random.randint(1,1000))

#lista exportalasa
with open("szamok.txt","w", encoding="utf-8")as adatfolyam:
    print(*szamlsita, sep=";", file=adatfolyam)

#importalas
with open("szamok.txt","r", encoding="utf-8")as adatfolyam:
    szamok = adatfolyam.read()

szamok = szamok.split(";")

'''for szam in szamok:
    print(szam)'''

szamok.sort()
parosok = []

for x in szamok:
    if int(x) % 2 ==0:
        parosok.append(x)