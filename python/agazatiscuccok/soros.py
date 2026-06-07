import math

# Olvass be egy szövegfájlt (nevét a felhasználó adja meg)! Írd ki soronként a sorok tartalmát sorszámmal együtt, a sorok számát, a leghosszabb sort, és hogy összesen hány szó van a fájlban. Kezeld, ha a fájl nem létezik!

def megynyit(fajlnev):
    with open(fajlnev, "r",encoding="utf-8")as adat:
        szoveg = adat.read()
        return szoveg
    
szoveg = megynyit("teszt.txt")

sorok = szoveg.split("\n")
szavak = szoveg.split()
index = 0

for x in sorok:
    index += 1
    print(x, index) 


leghosszabbsor = sorted(sorok, key=len)[-1]

print(leghosszabbsor)
