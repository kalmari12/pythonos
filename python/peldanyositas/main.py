from osztalyok import szemely

szemelyek = []

hany = int(input("Hány nevet fog megadni: "))

for ember in range(hany):
    vezeteknev = input("Adja meg a vezeteknevet: ")
    kereszt = input("Adja meg a keresztnevet: ")
    while vezeteknev != "nem" or kereszt != "nem" or :    
        szemelyek.append(szemely(vezeteknev, kereszt))

print(szemelyek)



