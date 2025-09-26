import random

szam1_sorsol_uj = True

while szam1_sorsol_uj:
    print(f"Szám: {random.randint(1, 200)}")
    kerdes = str(input("Sorsoljak még egy számot: (i/n)"))
    if kerdes == 'n':
        szam1_sorsol_uj = False
print(">>> Program vége <<<")

