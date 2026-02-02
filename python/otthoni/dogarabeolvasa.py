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


with open("egricsillagok.txt", "r", encoding="utf-8")as data:
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
