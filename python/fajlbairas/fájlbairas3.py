import random

szamlista = []

for _ in range(1000):
    szamlista.append(random.randint(1,10000))

szamlista.sort()

kiirando = ", ".join(map(str, szamlista))

with open('kimenet3.txt',  'w', encoding="utf-8") as adatfolyam:
    print(kiirando)
    print(kiirando, file=adatfolyam)