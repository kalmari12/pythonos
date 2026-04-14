with open("python/ekirasosbeolvasas/fajl.txt","r",encoding="utf-8")as adat:
    szoveg = adat.read()


jelek = [",",".","-","_","(",")","?",";",":","[","]"]

for jel in jelek:
    szoveg = szoveg.replace(jel,"")

szavak = szoveg.strip().lower().split()

# 1. feladat

abetusok = []

for szo in szavak:
    if szo[0] == "a" and szo not in abetusok:
        abetusok.append(szo)

# 2. feladat

print(abetusok,"\n",40*"-","\n", len(abetusok),"\n",40*"-")

# 3. feladat

bcdlista = []

for szo in szavak:
    if szo[0] == "b" and szo not in bcdlista:
        bcdlista.append(szo)
    if szo[0] == "c" and szo not in bcdlista:
        bcdlista.append(szo)
    if szo[0] == "d" and szo not in bcdlista:
        bcdlista.append(szo)

# 4. feladat

print("\n",40*"-","\n",bcdlista,"\n",40*"-","\n", len(bcdlista))

# 5. feladat

with open("python/ekirasosbeolvasas/fajl.txt","r",encoding="utf-8")as adat:
    szoveg = adat.read()

mondatok = szoveg.split(".")

print("\n",40*"-","\n", len(mondatok))

# 6. feladat

bekezdesek = szoveg.split("\n") ; print("\n",40*"-","\n", len(bekezdesek))

# 7. feladat

legrovidebb = sorted(bekezdesek, key=len,reverse=True)

print("\n",40*"-","\n",legrovidebb[-1])

# 8.

legmondat = sorted(mondatok, key=len)

print("\n",40*"-","\n",legmondat[-1])


