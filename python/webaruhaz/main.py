from modul import termek

termekek = []

def atlag(lista: list) -> float:
    ossz = 0
    index = 0
    for x in lista:
        index += 1
        ossz += int(x.AR_HUF)
    return ossz / index

with open("python/webaruhaz/webaruhaz_termekkatalogus.csv","r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat:
        termekek.append(termek(sor))
    
print(atlag(termekek))


legkisebb_ar = termekek[0]

index = 0

while index < len(termekek):
    if termekek[index].AR_HUF < legkisebb_ar.AR_HUF:
        legkisebb_ar = termekek[index]
    index += 1

bekert = "PROD004"

index = 0
talat = True


while talat:
    if termekek[index].Termek_ID == bekert:
        print(f"A bekert id-s elem: \n{termekek[index]}")
        talat = False
    index += 1

if talat == True:
    print("Nincs ilyen termek!")

