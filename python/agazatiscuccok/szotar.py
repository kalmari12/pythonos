szoveg = "A ház nagy. A ház szép. A szép ház nagy és régi."

def tisztit(adat: str):
    for x in [".",",",">","<","-","+","!","?",";","/","(",")","[","]"]:
        adat = adat.replace(x,"")
    adat = adat.lower()
    return adat

szavak = tisztit(szoveg).split()
  
print(szavak)

szavak2 = {}
                                             
def idk(idk: str, lista: dict):
    for x in idk:
        lista[x] = lista.get(x,0) +1
    return lista

print(idk(szavak,szavak2))
    
