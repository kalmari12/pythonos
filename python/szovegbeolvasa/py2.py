import random 

with open("mirage.txt", "r", encoding="utf-8")as fajl:
    szoveg = fajl.read()

elvalasztok = [".", ",",";",":","\n","_","?","!","(",")","[","]"]

for szo in elvalasztok:
    szoveg = szoveg.replace(szo, " ")

#csupa kisbetu
szoveg = szoveg.lower()

#szavak listaba toltese szokozok alapjan
szavak = szoveg.split()

sznelkul = []

for szo in szoveg:
    if szo != " ":
        sznelkul.append(szo)

szavak = sznelkul

print(szavak)