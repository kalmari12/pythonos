with open("forrasbejaras.txt", "r")as adat:
    szamok = adat.read()

print("A fájl beolvasva")

tartalom = szamok.strip().split("*")

'''
for szam in tartalom:
    print(szam)
'''

'''
print(*tartalom, sep=" / ")
'''



#A megoldas
index = 0

for szam in tartalom:
    if int(szam) == 11907:
        index += 1

print(f"A keresett szam ennyiszert szerepel: {index}")

#B megoldas
index = 0
kereses = input("Adja meg melyik szamot keressem: ")

for szam in tartalom:
    if szam == kereses:
        index += 1


print(f"A keresett szam ennyiszert szerepel: {index}")