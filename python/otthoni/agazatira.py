import random

# 1. Kérj be két egész számot, majd írd ki az összegüket.

szam1 = random.randint(1,9)
szam2 = random.randint(1,9)

print(f"Az első megadott szám: {szam1}")
print(f"A második megadott szám:  {szam2}")

# 2. Kérj be két egész számot, majd írd ki a különbségüket.

kulonbseg = szam1 - szam2

print(f"A két szám különbsége: {kulonbseg}")

# 3. Kérj be egy számot, és írd ki a négyzetét.

negyzet = szam1**2

print(f"A megadott szám négyzete: {negyzet}")

# 4. Kérj be egy oldalt (a), majd számold ki a négyzet kerületét.

oldal1 = random.randint(1,9)

terulet = oldal1**2

print(f"A négyzet területe: {terulet}")

# 6. Kérj be egy életkort, majd írd ki, hány éves lesz 5 év múlva.

eletkor_most = random.randint(1,100)

eletkor_utana = eletkor_most + 5

print(f"Az ön életkora öt év múlva: {eletkor_utana}")

# Kérj be egy Celsius-fokot, majd számold ki Fahrenheitben (F = C * 1.8 + 32).

Cfok = random.randint(1,100)

ffok = Cfok * 1.8 + 32

print(f"A megadott celsius farenheit ben : {ffok:.0f}")

# 8. Adott lista: szamok = [3, 6, 2, 9, 4]. Írd ki a lista elemeit egymás alá.

szamok = [3, 6, 2, 9, 4]

print(f"A lista elemei egymás alatt: ")

for szam in szamok:
    print(szam)

# 9. Írd ki, hány eleme van a szamok listának.

print(f"A szamok listanak {len(szamok)} eleme van")

# 10. Írd ki a szamok lista legnagyobb elemét.

print(f"A szamok listanak a legnagyobb eleme: {max(szamok)}")

# 11. Számold ki a szamok lista elemeinek összegét.

print(f"A szamok lista elemeinek osszege: {sum(szamok)}")

# 12. Készíts új listát, amely csak a páros számokat tartalmazza a szamok listából.

listap = []

for szam in szamok:
    if szam % 2 == 0:
        listap.append(szam)

print(listap)

# 13. Add hozzá a 10 számot a szamok lista végéhez, majd írd ki.

for x in range(10):
    szamok.append(random.randint(1,9))

print(szamok)

# 14. Ellenőrizd, hogy a 7 benne van-e a szamok listában

het = 0

while het <= 0:
    for szam in szamok:
        if szam == 7:
            het += 1
            print("A hét benne van a listaban")

# 15. Számold meg, hány pozitív szám van a szamok listában.
hszamok = 0

for szam in szamok:
    if szam > 0:
        hszamok += 1

print(f"Ennyi pozitiv szam van a listaban: {hszamok}")

# 16. Írj egy függvényt, amely kiírja: Szia!

def koszones_nyomtatas():
    print("Szia")

koszones_nyomtatas()

# 17. Írj egy függvényt, amely két számot kap és visszaadja az összegüket.

elsoszam = random.randint(1,9)
masodszam = random.randint(1,9)

def ket_osszeg(a,b):
    return (a + b)

print(ket_osszeg(elsoszam, masodszam))

# 18. Írj egy függvényt, amely eldönti egy számról, hogy páros-e.

x = 2
def paros_e(x):
    eredmeny = False
    if x % 2 == 0:
        eredmeny = True
    return eredmeny

print(paros_e(2))