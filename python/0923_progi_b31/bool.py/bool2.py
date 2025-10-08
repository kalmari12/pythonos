import random

szam1 = random.randint(1, 3)

szam2 = random.randint(2, 4)

eredmeny = szam1 == szam2

if eredmeny == True:
    print(f"A két szám egyenlő!\n"
          f"Az első szám: {szam1}\n"
          f"A masodik szam: {szam2}")

else:
    print("A két szám nem egyenlő")