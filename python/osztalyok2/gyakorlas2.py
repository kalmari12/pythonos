import random

with open("szalasanyagok.txt","r",encoding="utf-8")as adat:
    szoveg = adat.read()

jelek = [",",".","-","_","[","]",":","?",";","*","(",")"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower().strip().split()

# hany szo van a szovegben

print(f"Ennyi szo van a szovegben: {len(szoveg)}")

# megadott szo megkeresese

index = 0
megadott = str(input("Adja meg a keresendo szot: "))

for szo in szoveg:
    if szo == megadott:
        index += 1

if index > 0:
    print(f"A megadott szo ennyiszer szerepel a listában: {index}")
else:
    print("A megadott szó nem szerepel a listában")

# minta megkeresese

minta = str(input("adja meg a keresendo mintat: "))
mintak = []

for szo in szoveg:
    if minta in szo:
        mintak.append(szo)

print(f"ezekben a szavakban talalhato meg a minta: {mintak}")

# random indexu elem megtalalasa

index = 0
indexu = random.randint(1, len(szoveg))

for szo in szoveg:
    if szo == szoveg[indexu]:
        index += 1

print(f"A megadott indexu elem: {szoveg[indexu]}. Ennyiszer talalato a megadott indexu elem a listában: {index}")

# a megadott kezdobetuvel kezdodo szo megkereseese

adja = str(input("Adja meg a kezdobetut: "))
megadottlista=[]

for szo in szoveg:
    if szo[0] == adja:
        megadottlista.append(szo)

print(f"A megadott kezdobetuvel kezdodo szavak: {megadottlista}")

# megadott kezdobetuju es uccsobetu
uccsobetu = str(input("Adja meg a uccsobetut: "))
index = 0
kezdoslista = []

for szo in szoveg:
    if szo[0] == adja and szo[-1] == uccsobetu:
        index += 1  
        kezdoslista.append(szo)

print(f"A megadott kezdobetuvel es uccsobetuvel ennyi szo van: {index}\n\n"
      f"Ezekben a szavakban van benne a: {kezdoslista}")

with open("./python/osztalyok2/listagenyo.txt","w",encoding="utf-8")as adatfolyam:
    print(*szoveg, file=adatfolyam)