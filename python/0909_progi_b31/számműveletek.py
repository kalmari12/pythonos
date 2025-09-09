szam = int(input("Kérek egy számot: "))

if szam > 143:
    print(f"Túl nagy szám!")
elif szam  < 0:
    print(f"Túl kicsi szám")
else:    

    hatvany = szam ** szam 

    print(f"A szám önmagára emelt hatvanya: {hatvany}\n"
          f"A Számjegek szama: {len(str(hatvany))}\n"
          f"A számjegyek száma osztava a számmal: {hatvany/len(str(hatvany))}")
