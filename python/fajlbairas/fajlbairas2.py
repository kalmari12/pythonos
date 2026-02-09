import random

szamlista = []

for _ in range(100):
    szamlista.append(random.randint(1,100))

szamlista.sort()

kiirando = ", ".join(map(str, szamlista))

with open('kimenet2.txt',  'w', encoding="utf-8") as adatfolyam:
    print(f"{szamlista}", sep=', ', file=adatfolyam)



























'''for _ in range(100):
    with open('kimenet2.txt', 'a', encoding="utf-8") as datafolyam:
        szam = random.randint(1, 100)
        print(f"{szam}")
        print(f"{szam}", file=datafolyam)
'''