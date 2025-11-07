import random

szamlista = []

for x in range(500):
    szamlista.append(round(random.random()))

print(szamlista)
 
egyesek = []
index = 0

for i in range(len(szamlista) - 2):
    if szamlista[i] == 1 and szamlista[i+1] == 1 and szamlista[i+2] == 1:
        index+= 1

print(f"A 111 minta ennyiszer fordul elo a listaban: {index}")













