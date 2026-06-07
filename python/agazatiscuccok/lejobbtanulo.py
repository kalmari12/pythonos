import random

# Írj programot, amely bekér a felhasználótól 5 nevet és hozzá tartozó pontszámot (0–100)! Mentse ezeket egy .txt fájlba (soronként 'név:pontszám' formátumban)! Majd olvassa vissza és írja ki a legjobb eredményt elért tanulót.

nevek = []

with open("tanulok.txt","w",encoding="utf-8")as adat:
    for x in range(5):
        nev = str(input("Adja meg a tanulo nevet: "))
        nevek.append(nev)
        pont = int(input("Adja meg a tanulo pontszamat: "))
        nevek.append(pont)
        #print(f"{nev, pont}",file=adat)
        adat.write(f"{nev,pont}")
        
