from osztalyok import osztaly
import csv

termekek2 = []
termekek = []


'''with open("python/termekek/termekek_hardver_szoftver.csv","r",encoding="utf-8")as adat:
    next(adat)

    for sor in adat:
        adatok = sor.strip().split(","); id = adatok[0]; nev = adatok[1]
        kategoria = adatok[2]
        ar = adatok[3]
        mennyiseg = adatok[4]
        leiras = adatok[5]
        t = osztaly(id,nev,kategoria,ar,mennyiseg,leiras)
        termekek.append(t)'''



with open("python/termekek/termekek_hardver_szoftver.csv","r",encoding="utf-8")as adat:
    reader = csv.DictReader(adat)
    for sor in reader:
        termekek.append(osztaly(sor["id"].strip(), sor["nev"].strip(),sor["kategoria"].strip(), sor["ar"].strip(),sor["mennyiseg"].strip(),sor["leiras"].strip()))

print(termekek2)
    
