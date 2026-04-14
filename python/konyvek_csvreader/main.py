from classs import konyv
import csv

konyvek = []

with open("python/konyvek_csvreader/konyvek.csv","r",encoding="utf-8")as adat:
    reader = csv.DictReader(adat)

    for sor in reader:
        k = konyv(sor["cim"],sor["szerzo"],sor["ISBN"],sor["megjelenes_eve"],sor["oldalszam"])
        konyvek.append(k)

for konyv in konyvek:
    print(konyv,"\n",40*"-")

print(f"Az atlag oldalszam: {konyv.atlagkonyv(konyvek)}")