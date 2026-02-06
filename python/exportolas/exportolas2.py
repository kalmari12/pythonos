import random

szamok = []

for x in range(500):
    szamok.append(random.randint(1,1000))

with open("ideirom2.txt","w", encoding="utf-8")as datafolyam:
    print(*szamok, file=datafolyam)

with open("ideirom2.txt", "r", encoding="utf-8")as adatfolyam:
    importolt = adatfolyam.read()

importolt = importolt.split()