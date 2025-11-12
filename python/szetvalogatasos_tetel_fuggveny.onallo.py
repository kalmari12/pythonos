import random

lista = []
paros2 = []
paratlan = []
idk = []
sima = []

for x in range(100):
    lista.append(random.randint(1,45))

def osszeg():
    for x in lista:
        if x % 2 == 0:
            paros2.append(x)
        else:
            idk.append(x)
    return osszeg

paratlan = osszeg()
sima = osszeg()

paros2.sort()
idk.sort()

print(paros2)
print(idk)

print(len(paros2))
print(len(idk))