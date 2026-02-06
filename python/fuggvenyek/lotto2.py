import random 

def sorsol(hány = int(6), mettől = int(1), meddig = int(45)) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
        lista.sort()
    return lista



for x in range(52):
    számlista = sorsol()
    print(f"{x+1}. heti hatos lotto szamai: {számlista}")

