from classok import szemely
import csv

szemelyek = []

'''with open("python/otthoniclassok/szemelyek_bov.csv","r",encoding="utf-8")as data:
    next(data)

    for sor in data:
        adatok = sor.strip().split(",")
        nev = adatok[0]
        szulhely = adatok[1]
        szuldatum = adatok[2]
        email = adatok[3]
        telefonszam = adatok[4]
        iranyitoszam = adatok[5]
        varos = adatok[6]
        utca = adatok[7]
        hazszam = adatok[8]
        nem = adatok[9]
        allampolgarsag = adatok[10]
        szemelyi_azonosito = adatok[11]
        anyja_neve = adatok[12]
        sz = szemely(nev,szulhely,szuldatum,email,telefonszam,iranyitoszam,varos,utca,hazszam,nem,allampolgarsag,szemelyi_azonosito,anyja_neve)
        szemelyek.append(sz)


for sz in szemelyek:
    print(sz)'''


szemelyek2 = []
nok = []

with open("python/otthoniclassok/szemelyek_bov.csv","r",encoding="utf-8")as data:
    reader = csv.DictReader(data)
    for sor in reader:
        szemelyek2.append(szemely(sor["nev"],sor["szulhely"],sor["szuldatum"],sor["email"],sor["telefonszam"],sor["iranyitoszam"],sor["varos"],sor["utca"],sor["hazszam"],sor["nem"],sor["allampolgarsag"],sor["szemelyi_azonosito"],sor["anyja_neve"]))

for szemely in szemelyek2:
    if szemely.nem == "nő":
        nok.append(szemely)

for szemely in nok:
    print(szemely)