szöveglista = []

# forrás beolvasása
with open('forras2.txt', 'r', encoding='utf-8') as befájl:
    szöveg = befájl.read()
    szöveglista = list(map(str, szöveg.strip().split(" ")))
     
for szó in szöveglista:
    if szó[-1] == "." or szó[-1] == ",":
        szöveglista = [szó.rstrip(".,") for szó in szöveglista]

szöveges = []
# forrás beolvasása csak megjelenitésre
for x in szöveglista:
    print(x)

for x in szöveglista:
    if x[0] == "a" or x[0] == "A":
        szöveges.append(x)
        with open("python/forras3.txt", "a", encoding="utf-8") as onallogenyo:
            print(x, file=onallogenyo)
            print("A fájl elkászült")


# bcd betuvel kezdodo szavak

bcdlista = []

for szó in szöveglista:
    if szó[0] == "b" or szó[0] == "B" or  szó[0] == "C" or szó[0] == "c" or  szó[0] == "d" or szó[0] == "D":
        bcdlista.append(szó)

print(bcdlista)

# hany szo vegzodik n el és melyek azok

nlista = []

for szó in szöveglista:
    if szó[-1] == "n" or szó[-1] == "N":
        nlista.append(szó)

print(f"Ennyi szo vegzodik n-el: {len(nlista)}, ezek a szavak kezdodnek n-el: {nlista}")

# hany szo tartalmaz k vagy K-t

kindex = 0
megnezes = bool(True)
loindex = 0
hindex = 0

for szó in szöveglista:
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

# mely szavak harom betusek

haromszavak = []

for szó in szöveglista:
    if len(szó) == 3:
        haromszavak.append(szó)

print(haromszavak)

# mely szavak tartalmazzak az altalad megadott mintat

idklista =  []
idk = str(input("adjon meg egy mintat"))

for szó in szöveglista:
    if idk == szó[0:len(idk)]:
        idklista.append(szó)

print(idklista)



































     







































