with open("szalasanyagok.txt","r",encoding="utf-8")as data:
    szoveg = data.read()

jelek = [".","-",",",":",";",">","_","!","?","[","]",]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower().strip().split()

#

print(f"Ennyi szo van a szovegben: {len(szoveg)}")

#megadott szó megkeresese

megadott =  str(input(f"Adja meg a keresendo szot:"))
index = 0

for szo in szoveg:
    if szo == megadott:
        index += 1

if index > 0:
    print(f"A megadott szo ennyiszer szerepel a listban: {index}")
else:
    print("A megadott szo nem szerepel a listában.")

# a betus szavak keresese a litaban
index = 0
abetusok = []

for szo in szoveg:
    if szo[0] == "a":
        index += 1
        abetusok.append(szo)        

# abetus lista kiiratasa masik fajlba 

with open("./python/osztalyok2/abetusok.txt", "w", encoding="utf-8")as adatok:
    print(*abetusok, sep=" - ", file=adatok)

# minden harom betus szo keresese

harmasok = []

for szo in szoveg:
    if len(szo) == 3:
        harmasok.append(szo)

print(f"Ezek a szavak harombetusek: {harmasok}")

# megadott indexu szo kikeresese
index = 0

indexu = int(input("Adja meg hanyadik indexu szot keressem meg(pl.: 1,2,3....stb): "))

print(f"A megadott indexu elem: {szoveg[indexu]}")

for szo in szoveg:
    if szo == szoveg[indexu]:
        index += 1

print(f"Ennyi megadott idexu elem van a listaban: {index}")

# 

