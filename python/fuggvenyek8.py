import random 

def sorsol() -> list:
    hány = int(input("hány számot sorsoljak: "))
    mettől = int(input("Mettől sorsoljak: "))
    meddig = int(input("Meddig sorsoljak: "))
    lista = []
    for x in range(hány):
        lista.append(random.randint(mettől, meddig))
    return lista


számlista = sorsol()
print(f"lista elemei: {számlista}")






