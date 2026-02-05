import random

szamlistA = []
for _ in range(500):
    szamlistA.append(random.randint(1, 1000))

# lista exportálása
with open('számok.txt', 'w', encoding='utf-8') as adat:
    print(*szamlistA, sep=';', file=adat)

# importálás
with open('számok.txt', 'r', encoding='utf-8') as adat:
    szamokIMPORT = adat.read()

szamokIMPORTlista = szamokIMPORT.split(';')

'''for x in szamokIMPORTlista:
    print(x)'''

paros = []

for x in szamokIMPORTlista:
    if int(x) % 2 == 0:
        paros.append(x)