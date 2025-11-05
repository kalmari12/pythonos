####### A MEGOLDÁS #######
#l-> nincs visszatérési érték - "alprogram"
#függvény definíció

def kiir():#függvény neve, zárójelben az attribútumok
    print("Teszt") # ami a függvénmy hívása során működik

#függvény (meg)hívása 

kiir()
kiir()
kiir()

##########################

####### B MEGOLDÁS #######
#l-> szabványos függvény
def kiir2(a):
    return a #ez egy függvényérték (visszatérési érték)

print(kiir2("alma"))

def össz(a, b) -> int:
    összeg = a + b
    return összeg # mindig valaminke azt értéke változónévvel lehivatkozva

def össz2( a =int(10),b = int(12)) -> int:
    return a + b


print(össz2())

def egyenlet(a, b, c, d) -> float: # alapértelmezés nélküli függvény 
    eredmény = a*b*c+(d/c)+(a*d)+b-(d*a)
    return eredmény

print(f"Eredmény: {egyenlet(34, 56, 78, 92):.2f}")

def egyenlet2(a, b, c, d = int(100)) -> float: # a "d" alapértelmezett érték
    eredmény2 = a*b*c+(d/c)+(a*d)+b-(d*a)
    return eredmény2

a = int(input("Add meg az a szamot: "))
b = int(input("Add meg a b szamot: "))
c = int(input("Add meg a c szamot: "))
print(f"Eredmény: {egyenlet2(a, b, c):.2f}")






