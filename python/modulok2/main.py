from osztalyok import termek
import csv

'''ttermek1 = termek("Paradicsom",45,"Zöldség",139)

print(ttermek1)'''

'''termekek = [
     termek("Paradicsom",45,"Zöldség",139), termek("repa",424252,"Zöldség",60), termek("Narancs",12372462,"Gyümölcs",200)
]

print(termekek[0].nev) #Első példány neve (mert az osztály definíciónál létezik ilyen tulajdonság)'''

'''ttermek = termek("Ram","Elektronika",100000)

print(ttermek)'''

termekek = [

]

'''with open("python/modulok2/termekek_hardver_szoftver.csv", "r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        szoveg = adat.read()
        sorok = szoveg.split(",")
        id = sorok[0]
        nev = sorok[1]
        kategoria = sorok[2]
        ar = sorok[3]
        mennyiseg = sorok[4]
        leiras = sorok[5]

        t = termek(id,nev,kategoria,ar, mennyiseg, leiras)
        termekek.append(t)

for termek in termekek:
    print(*termekek, sep="\n")
'''

    




with open("python/modulok2/termekek_hardver_szoftver.csv", "r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        adatfolyam = sor.strip().split(',')
        id = adatfolyam[0]
        nev = adatfolyam[1]
        kategoria = adatfolyam[2]
        ar = adatfolyam[3]
        mennyiseg = adatfolyam[4]
        leiras = adatfolyam[5]

        t = termek(,nev, kategoria, ar)
        termekek.append(t)

for termek in termekek:
    print(termek)

    