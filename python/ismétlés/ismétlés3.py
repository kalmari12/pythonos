import random

szám = random.randint(-200, 200)

print(f"sorsolt szam: {szám}\n"
      f"--------------------\n"
      f"")

if szám < 0:
    print(f"A szám kisebb mint 0")
elif szám > 0:
    print(f"A aszam pozitiv")
else:
    print(f"a szam pontosan nulla")

if szám % 2 == 0:
    print(f"A szam paros")
else:
    print("a szam paratlan")

















