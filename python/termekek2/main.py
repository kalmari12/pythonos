from fontosak import termek
import csv

termekek = []
termekek2 = []

'''with open("python/termekek2/termekek_hardver_szoftver.csv", "r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        adatok = sor.strip().split(",")
        t = termek(adatok[0],adatok[1],adatok[2],adatok[3],adatok[4],adatok[5])
        termekek.append(t)'''

with open("python/termekek2/termekek_hardver_szoftver.csv", "r",encoding="utf-8")as adat:
    reader = csv.DictReader(adat)
    for sor in reader:
        t = termek(sor["id"].strip(),sor["nev"].strip(),sor["kategoria"].strip(),sor["ar"].strip(),sor["mennyiseg"].strip(),sor["leiras"].strip())
        termekek2.append(t)

print(termekek2)