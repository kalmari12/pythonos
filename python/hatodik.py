szam1 = int(input("kérek egy számot: "))

if szam1 <= 500 and szam1 >= -500:

    print(f"A szám 500 vagy annál kisebb és mínusz 500 vagy annál nagyobb!")
elif szam1 < -500:
    print(f"A szám kisebb mint -500!")
else:
    print(f"A szám nagyobb 500-nál!")


