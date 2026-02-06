with open("challenger.txt","r",encoding="utf-8")as adat:
    szoveg = adat.read()

jelek = [",", ">",":",";","_","-","[","]","(",")"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

bekert = str(input("Adjon meg egy szot: "))

megvan = szoveg.count(bekert)

print(megvan)

'''index = 0

for szo in szoveg:
    if szo == bekert:
        index += 1

if index > 0:
    print(f"A szó ennyiszer található meg a szövegben: {index}")
else:
    print("A szó nem talalható meg a szövegben")
'''
minta = str(input("Kérem adja meg a keresendo mintat: "))
mintak = []

for szo in szoveg:
    if minta in szo:
        mintak.append(szo)

print(f"{mintak}")

index =0
szamoklista  = []

for szo in szoveg:
    if szo.isdigit():
        index += 1
        szamoklista.append(szo)

oszthato = []

for szam in szamoklista:
    if int(szam) % 2 == 0:
        oszthato.append(szam)

print(f"osztahtok: {oszthato}")

print(f"ennyi szám van a szövegben: {index}")
        
insa = []

for szam in szamoklista:
    if isinstance(int(szam), int):
        insa.append(int(szam))


print(insa)