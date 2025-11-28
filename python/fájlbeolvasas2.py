with open('forrás.txt', 'r', encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()

szoveglista = list(map(str, tartalom.split(" ")))

szoveglista = [szó.strip(".,") for szó in szoveglista] # eltávolitja a szo vegerol és az elejerol is
#print(szamok)

szoveglista = [szó.rstrip(".,") for szó in szoveglista] # rear strip, csak a vegerol torli ki

for x in szoveglista:
    print(x)

print(f"A szavak szama a forrasban: {len(szoveglista)}")

# hany a betuvel kezdodo szo van a listaban

abetusszavak = []

for szó in szoveglista:
    if szó[0] == "a" or szó[0] == "A":
        abetusszavak.append(szó)

print(abetusszavak)

# bcd betuvel kezdodo szavak

bcdlista = []

for szó in szoveglista:
    if szó[0] == "b" or szó[0] == "B" or  szó[0] == "C" or szó[0] == "c" or  szó[0] == "d" or szó[0] == "D":
        bcdlista.append(szó)

print(bcdlista)

# hany szo vegzodik n el és melyek azok

nlista = []

for szó in szoveglista:
    if szó[-1] == "n" or szó[-1] == "N":
        nlista.append(szó)

print(f"Ennyi szo vegzodik n-el: {len(nlista)}, ezek a szavak kezdodnek n-el: {nlista}")

# hany szo tartalmaz k vagy K-t

kindex = 0
megnezes = bool(True)
loindex = 0
hindex = 0

for szó in szoveglista:
    megnezes = bool(False)
    for x in szó:
        if not megnezes and x == "k" or x == "K":
            kindex += 1
            megnezes = bool(True)
    if szó.__contains__("lo"):
        loindex += 1
    if len(szó) == 3:
        hindex += 1

print(f"Ennyi szo all harom karakterbol {hindex}")
print(f"Ennyi szo tartalmazza a mintat {loindex}")
print(f"Ennyi szó tartalmaz k-t: {kindex}")

# hány olyan szó van ami tartalmaz egy általad kitalált idk








