from gokart import Gokartpalya

palyak = []

with open("python/agazatiscuccok/gokart-adatok.txt","r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        adatok = sor.strip().split(";")
        palyak.append(Gokartpalya(adatok[0],adatok[1],adatok[2],adatok[3]))

ossz = 0

for x in palyak: ossz += int(x.palya_hossz)

print(sum([x.palya_hossz for x in palyak]))

legolcsobb = palyak[0].jegyar

for x in palyak: 
    if x.jegyar < legolcsobb:
        legolcsobb = x.jegyar
    if x.jegyar == legolcsobb:
        print(x)

print(Gokartpalya.aremeles("CsepelRing", palyak))



