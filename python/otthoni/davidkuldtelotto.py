# Lottó + export + import + nyerőszámok
import random

nyeresTable = []

def lotto(mettol, meddig, hanyas):
    hetszam = 0

    jatekosTippek = []
    tippek = 0
    while tippek <= hanyas:
        tipp = int(input(f'Kérem a(z) {tippek}. számot >>> '))
        if tipp not in jatekosTippek:
            jatekosTippek.append(tipp)
            print("Szám elfogadva.")
            tippek += 1
        else:
            print("A számod nem lett elfogadva!")

    ossznyeremeny = 0

    for x in range(52):
        nyeroszamok = []
        db = 0
        while db < hanyas:
            nyeroszam = random.randint(mettol, meddig)
            if nyeroszam not in nyeroszamok:
                nyeroszamok.append(nyeroszam)
                db += 1
        nyeresTable.append(nyeroszamok)

        hetszam += 1

        print(40*'-')
        print(f"A(z) {hetszam}. hét nyerőszámai: {nyeroszamok}")

        talalatok = 0
        for szam in jatekosTippek:
            for x in nyeroszamok:
                if szam == x:
                    talalatok += 1

        nyeremeny = 0
        if talalatok == 1:
            if hanyas == 5:
                nyeremeny = 1000
                ossznyeremeny += nyeremeny
            elif hanyas == 6:
                nyeremeny = 1500
                ossznyeremeny += nyeremeny
        elif talalatok == 2:
            if hanyas == 5:
                nyeremeny = 2000
                ossznyeremeny += nyeremeny
            elif hanyas == 6:
                nyeremeny = 3000
                ossznyeremeny += nyeremeny
        elif talalatok == 3:
            if hanyas == 5:
                nyeremeny = 5000
                ossznyeremeny += nyeremeny
            elif hanyas == 6:
                nyeremeny = 10000
                ossznyeremeny += nyeremeny
        elif talalatok == 4:
            if hanyas == 5:
                nyeremeny = 10000
                ossznyeremeny += nyeremeny
            elif hanyas == 6:
                nyeremeny = 25000
                ossznyeremeny += nyeremeny
        elif talalatok == 5:
            if hanyas == 5:
                nyeremeny = 25000
                ossznyeremeny += nyeremeny
            elif hanyas == 6:
                nyeremeny = 100000
                ossznyeremeny += nyeremeny
        elif talalatok == 6:
            if hanyas == 6:
                nyeremeny = 250000
                ossznyeremeny += nyeremeny

        print(f"Találatok száma: {talalatok}, nyereményed: {nyeremeny} Ft")
        print(40*'-')

    print(f"Az összes 52 hetes nyeremény: {ossznyeremeny} Ft")

lotto(1, 90, 5)

index = 0
turn = 0
while index < len(nyeresTable):
    with open('lottosorsolas.txt', 'a', encoding='utf-8') as data:
        turn += 1
        print(f"Az {turn}. heti nyerőszámok: {nyeresTable[index]}", sep='\n', file=data)
        index += 1