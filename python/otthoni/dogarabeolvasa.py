'''with open("egricsillagok.txt", "r", encoding="utf-8")as data:
    szoveg = data.read()
    
elvalasztok = [".",",","-","?",">",":",";"]

for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

minta = str(input("Kérem adjon meg egy mintat: "))
mintalista = []

for szo in szoveg:
    if minta in szo:
        mintalista.append(szo)

print(mintalista)
print(f"talalatok szama: {len(mintalista)}")

with open("minta.txt", "w", encoding="utf-8")as fajlok:
    print(mintalista, file=fajlok)'''


'''with open("egricsillagok.txt", "r", encoding="utf-8")as data:
    szoveg = data.read()

jelek = [".",",","-",":","?",";",">","*","\n"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

mintak = []
minta = str(input("Kérem adja meg a mintat: "))

for szo in szoveg:
    if minta in szo:
        mintak.append(szo)

print(f"ezekben a szavakban van meg a minta: {mintak}")

alista = []
alista2 = []

for szo in szoveg:
    if szo[0] == 'a':
        alista.append(szo)
        

for szo in alista:
    if szo not in alista2:
        alista2.append(szo)
    
print(alista2)
print(f"a-t tartalmazo szavak {alista}")
'''

'''
with open("egricsillagok.txt", "r", encoding="utf-8")as fajl:
    szoveg = fajl.read()

jelek = [",",".","-","?","_","!",";",">",";",">"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

mintak = []
minta = str(input("Adja meg a mintat: "))
index = 0

for szo in szoveg:
    if minta in szo:
        mintak.append(szo)
        index += 1

print(f"A minta ennyiszer talalhato meg a szövegben: {index}")
print(f"Ezeket a szavakat talaltuk amikben megvan a minta: {mintak}")

alista = []
aszam = 0

for szo in szoveg:
    if szo[0] == "a":
        alista.append(szo)
        aszam += 1

print(f"Ennyi szo kezdodik a-val: {aszam}")
print(f"Ezek a szavak kezdodnek a-val: {alista}")

'''

'''with open("egricsillagok.txt", "r", encoding="utf-8")as fajl:
    szoveg = fajl.read()

jelek = [",",".","-",">",";",":","_"]

for jel in jelek:
    szoveg = szoveg.replace(jel," ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

minta = str(input("adja meg a mintat: "))

mintak = []

for szo in szoveg:
    if minta in szo:
        mintak.append(szo)

print(f"Ezekben a szavakban talalhato meg a minta: {mintak}")'''

'''with open("mirage.txt", "r", encoding="utf-8")as data:
    szoveg = data.read()

jelek = [".",",","?",":",";","*","_","-","!"]

for jel in jelek:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveg = szoveg.strip().split()

tisztitott = []

for szo in szoveg:
    if szo != " ":
        tisztitott.append(szo)

harmas = []

for szo in szoveg:
    if len(szo) == 3:
        harmas.append(szo)

print(harmas)
'''
'''import random


szamok = []

for x in range(500):
    szamok.append(random.randint(1,1000))

with open("export.txt", "w", encoding="utf-8")as data:
    print(*szamok, sep=";",file=data)

szamokIMPORT = []

with open("export.txt", "r", encoding="utf-8")as adat:
    szamokIMPORT = adat.read()

szamokIMPORTLISTA = szamokIMPORT.split(";")
with open("export.txt","w", encoding="utf-8")as fileok:
    print(*szamokIMPORTLISTA, file=fileok)

'''
import random
szamok = []


for x in range(500):
    szamok.append(random.randint(1,1000))

with open("export.txt","w", encoding="utf-8")as data:
    print(*szamok, sep=";", file=data)

importlista = []

with open("export.txt","r",encoding="utf-8")as adat:
    importlista = adat.read()

importlistalista = importlista.split(";")

print(importlistalista)













