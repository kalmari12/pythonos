szoveg = str("A Német Lovagrend vagy Teuton Lovagrend (latinul Ordo Teutonicus, Ordo domus Sanctae Mariae Theutonicorum Ierosolimitanorum, vagy Ordo Teutonicus Sanctae Mariae in Jerusalem, németül Orden der Brüder vom Deutschen Haus St. Mariens in Jerusalem vagy Deutscher Orden) német egyházi-katonai lovagrend volt, amelyet eredetileg Palesztinában alapítottak betegápoló tevékenység céljából. Az Európába visszatérő lovagokat 1211–1225 között rövid ideig a Magyar Királyság területén, Dél-Erdélyben, a Borzaföldön (ma Barcaság) telepítette le II. András magyar király. Miután innen önállósodási kísérletük miatt kiverték őket, Konrád lengyel fejedelemtől kaptak új letelepedési lehetőséget, és a rend ettől kezdve elindult a felemelkedés útján. A balti pogány poroszok területeit fél évszázad alatt meghódítva, Marienburg székhellyel megalakították a Német Lovagrend független országát. A 13. századra már szinte az egész Baltikum a kezükre jutott. A lovagok azonban még több területet akartak, és folyamatosan támadták Lengyelországot és Litvániát. Előbbi esetében a háborút már nem leplezhették a kereszténység terjesztését célzó keresztes hadjárattal, mert a lengyelek katolikus keresztények voltak. A pogány litvánok ellen viszont térítőként léptek fel, az ortodox oroszokat pedig eretnekeknek tekintették, és ezen a címen indítottak ellenük háborút. Az 1410-es grünwaldi csata során azonban megsemmisítő vereséget szenvedtek, amely végleg eldöntötte a lovagok és a térség sorsát. Hatalmuk a következő időszakban fokozatosan összeomlott és meg kellett hódolniuk a lengyel királynak. A kegyelemdöfést azonban a reformáció jelentette, mivel az evangélikus hitre áttérő egyik nagymesterük kisajátította magának a rend kelet-porosz területeit, a livóniai részeken pedig a környező országok osztoztak. A rend a következő három évszázadban minden tekintélyét elvesztette, és 1809-ben Napóleon császár feloszlatta a máltai lovagrenddel együtt. Bár 25 év múlva újra létrehozták a német lovagrendet, azóta nem katonai rendként működik, hanem humanitárius tevékenységekre tért át. Ma már egyetlen lovagi tagjuk sincs, székhelyük Bécsben van.")


szoveg = szoveg.lower()

# nagybetűk: szoveg = szoveg.upper()
# Az első szó nagybetússé tevése: szoveg = szoveg.capitalize()

sk = [".",",","(",")"]

for jel in sk:
    szoveg = szoveg.replace(jel, "")

szoveglista = szoveg.split()

# for szo in szoveglista:
#     print(szo)¨

# megszámlálás

db = 0

for szo in szoveglista:
    if szo == "német":
        db += 1

# szétválogatás tétele: azok a szavak amik maganhangzoval kezdodnek

mghszavak = []
mghkarakterek = ['á','é','ő','ü','ó','ö','ű','í','o','e','a','u','ú']

for szo in szoveglista:
    if szo[0] in mghkarakterek and szo not in mghszavak:
        mghszavak.append(szo)


with open("python/string/mgh.txt", "w", encoding="utf-8")as adat:
    print(*mghszavak, sep=" // ",file=adat)
    print(F"\nA fájl elkészult")

with open("python/string/mgh.txt", "r", encoding="utf-8")as impfajl:
    importtartalom = impfajl.read()

print("\n az mgh.text tartalma:")
print(importtartalom)



































