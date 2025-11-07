def összeg(a,b) -> int:
    return a + b

def különbség(a,b) -> int:
    return a- b

def szorzat(a,b) -> int:
    return a*b

def hanyados(a,b)->float:
    return a/b

def maradek(a,b)->int:
    return a%b

beszam1 = int(input("Kérek egy számot: "))
beszam2 = int(input("Kérek egy másik számot: "))

print(f"A két szám összege: {összeg(beszam1, beszam2)}")
print(f"A két szám kulonbsege: {különbség(beszam1, beszam2)}")
print(f"A két szorzata összege: {szorzat(beszam1, beszam2)}")
print(f"A két szám hanyadoasa: {hanyados(beszam1, beszam2)}")
print(f"A két szám maradeka: {maradek(beszam1, beszam2)}")












