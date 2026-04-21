class konyv:
    def __init__(self, id, cim, szerzo, ar):
        self.id = id
        self.cim = cim
        self.szerzo = szerzo
        self.ar = ar

    def __str__(self):
        return f"A könyv azonosítója: {self.id}\nCíme: {self.cim}\nSzerzője: {self.szerzo}\nAra: {self.ar}"
    
    def oszlopkivetel(lista):
        listak = []
        for elem in lista:
            listak.append(elem.cim)
        return listak
    
    def atlagolas(lista):
        szamok = []
        index = 0
        for elem in lista:
            index +=1
            szamok.append(int(elem.ar))
        osszar = sum(szamok)
        return osszar/index