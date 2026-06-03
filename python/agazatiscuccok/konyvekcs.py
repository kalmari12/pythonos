elsoszam = int(input("Adja meg a kisebb szamot: "))
masodikszam = int(input("Adja meg a nagyobbik szamot"))

szamok = []

szamok.append(masodikszam)
szamok.insert(0,masodikszam)

for x in range(elsoszam, masodikszam):
    szamok.append(x)

print(*sorted(szamok),sep=", ")