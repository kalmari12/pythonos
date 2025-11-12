import random 

def sorsol(hány: int, mettől: int, meddig: int) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
    return lista


számlista = sorsol(5,1,90)
számlista2 = sorsol(100,1,300)

print(f"lista elemei: {számlista}")
print(f"- - -")
print(f"lista2 elemei: {számlista2}")
