import random

for x in range(100): # x = valtozo eldobasa, nem hasznaljuk fel, a szamokat nem taroljuk
    print(f"{random.randint(1, 1000)}")

#létrehozád
szamlista = []

#feltoltes
'''for _ in range(100):
    x = random.randint(1, 1000)
    if x in szamlista:
        pass
    else:
        szamlista.append(x)'''

#feltoltes mahgogy=(ugy hogy 100 legyen)
while len(szamlista) < 10000:
    x = random.randint(1,10000)
    if x not in szamlista:
        szamlista.append(x)


#rendezés
szamlista.sort()

#elemek kiiorasa a képernyore ellenorzesi céllal
print(f"elemek: {szamlista}")
print(f"elemek száma: {len(szamlista)}")

#lista bejárás 1
for x in szamlista:
    print(f"{x}")

#lista bejarasa 2
index = 0

while index < len(szamlista):
    print(f"{index + 1}. elem= {szamlista[index]}")
    index += 1













