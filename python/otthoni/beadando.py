import random

# 1. Kérj be két egész számot, majd írd ki az összegüket.

elsoszam = int(input("Kérek egy számot: "))
masodszam = int(input("Kérek egy másik számot: "))

ossz = elsoszam + masodszam

print(f"A két szám összege: {ossz}")

# 2. Kérj be két egész számot, majd írd ki a különbségüket.

print(f"A két szám különbsége: {elsoszam-masodszam}")

# 3. Kérj be egy számot, és írd ki a négyzetét.

print(f"Az első szám négyzete: {elsoszam**2}")

# 4. Kérj be egy oldalt (a), majd számold ki a négyzet kerületét.

oldala = int(input("adjon meg egy oldalt: "))

kerulet = oldala*4

print(f"A négyzet kerulete: {kerulet}")

# 5. Kérj be egy oldalt (a), majd számold ki a négyzet területét.

terulet = oldala**2

print(f"A negyzet terulete: {terulet}")

# 6. Kérj be egy életkort, majd írd ki, hány éves lesz 5 év múlva.

eletkor = int(input("Kéem adja meg az életkorát: "))

print(f"Ön {eletkor+5} éves lesz 5 év múlva")

# 7. Kérj be egy Celsius-fokot, majd számold ki Fahrenheitben (F = C * 1.8 + 32).

ffok = elsoszam*1.8 + 32

print(f"Az ön által megadott fok átváltva: {ffok}")

# 8. Adott lista: szamok = [3, 6, 2, 9, 4]. Írd ki a lista elemeit egymás alá.

szamok = [3, 6, 2, 9, 4]

for szam in szamok:
    print(szam)

# 9. Írd ki, hány eleme van a szamok listának.

print(f"A szamok listanak {len(szamok)} eleme van")

# 10. Írd ki a szamok lista legnagyobb elemét.

print(f"A szamok lista legnagyobb eleme: {max(szamok)}")

# 11. Számold ki a szamok lista elemeinek összegét.

print(f"A szamok lista osszege: {sum(szamok)}")

# 12. Készíts új listát, amely csak a páros számokat tartalmazza a szamok listából.

plista = []

for szam in szamok:
    if szam % 2 == 0:
        plista.append(szam)

print(plista)

# 13. Add hozzá a 10 számot a szamok lista végéhez, majd írd ki.

szamok.append(10)

print(szamok)

# 14. Ellenőrizd, hogy a 7 benne van-e a szamok listában.

for szam in szamok:
    if szam == 7:
        print("A hetes szam benne van a listaban")
    else:
        print("A hetes szam nincs benne a listban")

# 15. Számold meg, hány pozitív szám van a szamok listában.

index = 0

for szam in szamok:
    if szam > 0:
        index += 1

print(f"ennyi pozitiv szam van a listaban: {index}")

# 16. Írj egy függvényt, amely kiírja: Szia!

def koszones_szia():
    return print("szia")

koszones_szia()

# 17. Írj egy függvényt, amely két számot kap és visszaadja az összegüket.

def osszeadas_ketto(elso, masod):
    return elso + masod

print(osszeadas_ketto(elsoszam, masodszam))

# 18. Írj egy függvényt, amely eldönti egy számról, hogy páros-e.

randome = random.randint(1,9)

def paros_e(szame):
    if szame % 2 == 0:
        return "paros a szam"

print(paros_e(randome))

# 19. Írj egy függvényt, amely egy listát kap és visszaadja az átlagát.

def atlag_lista(lista):
    return sum(lista) / len(lista)

print(atlag_lista(szamok))

# 20. Írj egy függvényt, amely megszámolja, hány elem van egy listában.

def hany_elem(lista1):
    return len(lista1)

print(hany_elem(szamok))
