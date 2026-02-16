import random

'''szamlistA = []
for _ in range(500):
    szamlistA.append(random.randint(1, 1000))

# lista exportálása
with open('számok.txt', 'w', encoding='utf-8') as adat:
    print(*szamlistA, sep=';', file=adat)

# importálás
with open('számok.txt', 'r', encoding='utf-8') as adat:
    szamokIMPORT = adat.read()

szamokIMPORTlista = szamokIMPORT.split(';')

for x in szamokIMPORTlista:
    print(x)

paros = []

for x in szamokIMPORTlista:
    if int(x) % 2 == 0:
        paros.append(x)'''

'''
szamlista = []

for szam in range(500):
    szamlista.append(szam)

with open("export.txt","w",)as data:
    print(*szamlista, sep=" - ", file=data)

with open("export.txt","r")as adatfolyam:
    szamok = adatfolyam.read()

szamokimport = szamok.split(" - ")

parosok = []

for szam in szamokimport:
    if int(szam) % 2 == 0:
        parosok.append(szam)

print(parosok)

keress = 10

for szam in szamokimport:
    if int(szam) == keress:
        print("benne van")'''

top10_fajl = "top10.csv"

with open("python/otthoni/forrás.txt","r",encoding="utf-8")as data:
    szoveg = data.read()

karakterek = len(szoveg)

sorok = len(szoveg.split("\n"))

sorosok = szoveg.split("\n")

jelek = [",",".","-","_","[","]","=","(",")","?","!","{","}",";",":"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower().strip().split()

clean = szoveg

index = 0

for szo in clean:
    if szo == "Rock" or szo == "rock":
        index += 1

with open("python/otthoni/clean.txt", "w",encoding="utf-8")as adatok:
    print(*clean, file=adatok)

###########################################

szavak = []

for szo in clean:
    szavak.append(szo)

print(len(szavak))
print(szavak[:10])
print(szavak[-10:])

###########################

rovid_szavak = []
hosszu_szavak = []

for szo in szavak:
    if len(szo) < 4:
        rovid_szavak.append(szo)
    elif len(szo) > 10:
        hosszu_szavak.append(szo)


print(len(rovid_szavak))
print(len(hosszu_szavak))

###################

egyedi = []

for szo in szavak:
    if szo not in egyedi:
        egyedi.append(szo)

egyedi.sort()
print(len(egyedi))

####################

hosszvak = sorted(szavak, key=len, reverse=True)

print(hosszvak[:5])

######################

gyakorisag = {}

for szo in szavak:
    if szo in gyakorisag:
        gyakorisag[szo] += 1
    else:
        gyakorisag[szo] = 1

# rendezés gyakoriság szerint
rendezett = sorted(gyakorisag.items(), key=lambda elem: elem[1], reverse=True)

print("7. 10 leggyakoribb szó:")
for szo, db in rendezett[:10]:
    print(szo, "->", db)

# CSV mentés
fajl = open(top10_fajl, "w", encoding="utf-8")
fajl.write("szo,db\n")
for szo, db in rendezett[:10]:
    fajl.write(szo + "," + str(db) + "\n")
fajl.close()

print("Mentve:", top10_fajl)
print()

################################

evszamok = []

for szo in szavak:
    if len(szo) == 4 and szo.isdigit() and szo not in evszamok:
        evszamok.append(szo)

with open("python/otthoni/evszamok.txt","w")as adatfolyam:
    print(*evszamok,sep='---', file=adatfolyam)

#####################################

leghosszabb = []
legrovidebb = []

sortedsorosok = sorted(sorosok, key=len)

leghosszabb.append(sortedsorosok[-3:])
legrovidebb.append(sortedsorosok[:3])

####################################

with open("python/otthoni/riport.txt","w",encoding="utf-8")as riport:
    print(f"A karakterek száma: {karakterek}\nA szavak száma: {len(szavak)}\nEgyedi szavak száma: {len(egyedi)}\nTop ot leggyakoribb szo: {rendezett[:5]}\nevszamok: {evszamok}",file=riport)