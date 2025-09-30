import random

szamlista = []

#lista feltoltese veletlenszamokkal

for x in range(5000):
    szamlista.append(random.randint(-500, 500))

#lista kirasa

'''print(szamlista, sep="")'''

for x in szamlista:
    print(x, sep=" - ")







