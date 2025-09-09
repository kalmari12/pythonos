szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))

osszeg = szam1 + szam2 
hanyados = szam1 - szam2
szorzat = szam1 * szam2
hatvany = szam1 ** szam2
oszt = szam1 / szam2 
maradek = szam1 % szam2

print(f"A szamok osszege: {osszeg}\n\n"
      f"A szamok hanyadosa: {hanyados}\n\n"
      f" A szamok szorzata: {szorzat}\n\n"
      f"A szamok osztasa: {oszt:.2f}\n\n"
      f"A szamok hatvanya: {hatvany}")

if maradek > 0:
    print(f"A maradék nagyobb mint 0!")

if maradek > 5:
    print(f"A maradék nagyobb mint 5!")






'''
if maradek < 5:
    print(f"A maradek kisebb mint ot")
else:
    print(f"A maradék tobb mint ot")
'''
    





