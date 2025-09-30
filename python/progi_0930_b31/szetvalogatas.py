import random

szamlista = []

for x in range(100):
    szamlista.append(random.randint(0,500))

'''
szamlista.sort()
print(f"Növekvö sorrendbe elemek: {szamlista}\n") # novekvo lista (A szám listát is rendezi)
szamlista.sort(reverse=True) #csokkeno lista
print(f"CSökkeno sorrendbe elemek: {szamlista}")

# szétválogatás lista bejárással'''

harommal = []

ottel = []

hettel = []

kilencel = []

tizzel = []





#masik lehetoseg lenne 5 bejaras 5 viszgalattal ami eroforras igenyes de mukodne
for x in szamlista: # végig megyünk az összes elemen és megviszgáljuk őket
    if x % 3 == 0:
        harommal.append(x)
    if x % 5 == 0:
        ottel.append(x)
    if x % 7 == 0:
        hettel.append(x)
    if x % 9 == 0:
        kilencel.append(x)        
    if x % 10 == 0:
        tizzel.append(x)

harommal.sort()
ottel.sort()
hettel.sort()
kilencel.sort()
tizzel.sort()


print(f"\nHáromal oszthatók: {harommal}\n\n"
      f"ottel oszthatók: {ottel}\n\n"
      f"hettel oszthatók: {hettel}\n\n"
      f"kilencel oszthatók: {kilencel}\n\n"
      f"tizzel oszthatók: {tizzel}")
