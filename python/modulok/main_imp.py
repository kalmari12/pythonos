from modul import termek

termekek = []

with open("python/modulok/termekek.txt","r",encoding="utf-8") as adat:
    next(adat) # az első címsor kihagyasa

    for sor in adat:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        kategoria = adatok[1]

        t = termek(nev, kategoria)
        termekek.append(t)



print(f"Az első elem: {termekek[0]}")

for termek in termekek:
    termek.bruttoar =1000

for termek in termekek:
    termek.netto()

for termek in termekek:
    print(termek)