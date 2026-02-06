with open('kimenet3.txt', 'r', encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()

szamok = list(map(int, tartalom.split(",")))

#print(szamok)

for x in szamok:
    print(x)