from classok import konyv
import csv

konyvek = []

with open("python/2026.04.21.onallo.classok/konyvek.csv","r",encoding="utf-8")as adat:
    reader = csv.DictReader(adat)
    for sor in reader:
        konyvek.append(konyv(sor["id"],sor["cim"],sor["szerzo"],sor["ar"]))

Címek = konyv.oszlopkivetel(konyvek)

print(*Címek,sep=(" - "))

atlagar = konyv.atlagolas(konyvek)

print(f"atlagar: {atlagar:.0f}")