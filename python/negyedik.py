import math


a = int(input("Kérek egy számot: "))
b = int(input("Kérek egy másik számot: "))

hatvany = math.pow(a,b)

print(f"hatvány: {hatvany}")

gyök = math.sqrt(a)
print(f"gyök: {gyök:.2f}")
print(f"Gyök kerekítve: {math.ceil(gyök)}")

print(f" Az (a) szám típusa: {type(a)}")
print(f" Az (b) szám típusa: {type(b)}")
print(f" A hatvány típusa: {type(hatvany)}")
print(f" A gyök típusa: {type(gyök)}")



