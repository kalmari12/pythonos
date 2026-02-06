import random

szamlista = []

for szam in range(10000):
    szamlista.append(random.randint(1,50000))

# kiiras
'''print(*szamlista, sep=" ", end="\n\nA lista elkészült")'''

with open("forrasbejaras.txt","w")as adat:
    print(*szamlista, sep=" * ", file=adat)
    print(f"A fájl elkészult a kiirt elemk szama {len(szamlista)}")














