from fontosak import termek
import csv

termekek2 = []

with open("python/termekek2/termekek_hardver_szoftver.csv","r",encoding="utf-8")as adat:
    reader =csv.DictReader(adat)
    for sor in reader:
        t = termek(sor["id"].strip(),sor["nev"].strip(),sor["kategoria"].strip(),sor["ar"].strip(),sor["mennyiseg"].strip(),sor["leiras"].strip())
        termekek2.append(t)  

for sor in termekek2:
    print(sor)  
