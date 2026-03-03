#szöveg tisztítása
def tisztit(adatok):
    jelek = [",",":",".","_","?",";","!","%","[","]","(",")",'–']

    for jel in jelek:
        adatok = adatok.replace(jel, "")
    return adatok

#szöveg összes betűjét lowercase be rakja es szvakara bontja
def szavakbarakas(idk):
    idk = idk.lower().split()
    return idk

#egy felhasználó által megadott szó megkeresése
def kereses(adatok, megadott):
    index = 0

    for szo in adatok:
        if szo == megadott:
            index += 1
    return index

# a maganhangzókkal kezdődő szavak megkeresése
def maganhangzok(adatok):
    mghk = ["a","á","e","é","o","ó","ö","ő","u","ú","ü","ű","í"]
    talalt = []

    for szo in adatok:
        if szo[0] in mghk and szo not in talalt:
            talalt.append(szo)
    return talalt

#egyedi lista elkészítése
def egyedik(adatok):
    egyediek = []

    for szo in adatok:
        if szo not in egyediek:
            egyediek.append(szo)
    return egyediek

# évszámok keresése
def evszamozas(adatok):
    evszamok = []

    for szo in adatok:
        if szo.isdigit() and szamlalas(szo) >= 3:
            evszamok.append(szo)
    return evszamok

#szamok megkeresese
def szamok(adatok):
    szamok = []

    for szo in adatok:
        if szo.isdigit():
            szamok.append(szo)
    return szamok

#len nélkül megszámlálás
def szamlalas(adatok):
    index = 0
    for szo in adatok:
        index += 1
    return index



with open("python/arabcucc/forras.txt", "r", encoding="utf-8")as adat:
    szoveg = adat.read()

bekeres = str(input("Adja meg a keresendő szót: "))
szoveg = tisztit(szoveg)
szavak = szavakbarakas(szoveg)
mghszavak = maganhangzok(szavak)
egyediszavak = egyedik(szavak)
evszamok = evszamozas(szavak)
szamok = szamok(szavak)

print(evszamok)

if kereses(szavak,bekeres) > 0:
    print(f"A megkeresendő szó ennyiszer található meg a szövegben: {kereses(szavak, bekeres)}")
else:
    print(f"A listában nem található meg a keresendő szó")

with open("python/arabcucc/Listak.txt","w",encoding="utf-8")as adatfolyam:
    print(f"A magánhangzókkal kezdődő szavak listája: \n{mghszavak}\n\nAz egyedi szavak listája: \n{egyediszavak}\n\nAz évszámok listája: \n{evszamok}\n\nA számok listája: \n{szamok}", file=adatfolyam) 
