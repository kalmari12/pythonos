with open("challenger.txt", "r", encoding="utf-8")as fajl:
    szoveg = fajl.read() # fájl komplett tartalmának beolvasása

elvalasztok = [",",".","!","?","\n",";",":","[","]","(",")"]

for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")

#csupa kisbetu
szoveg = szoveg.lower()

#szavak listaba toltese szokozok alapjan
szavak = szoveg.split()

#ellenorzes - 1
print(f"Szavak száma: {len(szavak)}")

#ellenorzes - 2
tisztitott = []

for szo in szavak:
    if szo != "":
        tisztitott.append(szo)

szavak = tisztitott

#a betus szavakat szurunk
abetus = []

for szo in szavak:
    if szo[0] == "a":
        abetus.append(szo)

abetus.sort()

print(f"A vagy a betűvel kezdodo szavak, ennyi szo kezdodik a-val:{len(abetus)}, {abetus} ")


# felhasznalo altal megadott szavak keresese:

felh = str(input("Kérem adja meg a keresett szót: "))
index=0

for szo in tisztitott:
    if szo == felh:
        index += 1

if index > 0:
    print(f"A keresett szó benne van a listában. Ennyiszer szerepel a listában: {index}")











