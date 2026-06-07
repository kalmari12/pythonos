from classos import auto
import csv

autok = []

with open("python/agazatiscuccok/kemiai/hasznalt_autok.txt","r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        adatok = sor.strip().split()
        autok.append(auto(adatok[0],adatok[1],adatok[2],adatok[3],adatok[4],adatok[5],adatok[6]))

autok2 = [] 

with open("python/agazatiscuccok/kemiai/hasznalt_autok.csv","r",encoding="utf-8")as adatt:
    next(adatt)
    reader = csv.reader(adatt)
    for x in reader:
        autok2.append(auto(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))


print(autok2)

print(auto.atlag(autok))

print(auto.legkevesebb(autok))

idk = auto.uzemanyag2(autok,"Benzin")

#Készíts egy új listát fiatal_autok néven, amelybe csak a 2016 után gyártott autók kerülnek bele. Miután ez megvan, írd ki ezeknek az autóknak a márkáját, modelljét és árát egy új szöveges fájlba (fiatalok.txt), vesszővel elválasztva.
fiatal_autok = []

with open("python/agazatiscuccok/kemiai/Fiatal_autok.txt","w",encoding="utf-8")as adat:
    for x in autok:
        if x.gyartasiev > 2016:
            print(f"Marka: {x.marka}, Modell: {x.modell}, Ar: {x.ar}\n\n",file=adat)